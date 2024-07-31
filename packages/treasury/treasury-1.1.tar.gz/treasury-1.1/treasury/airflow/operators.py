from datetime import datetime, timedelta
from itertools import chain
import logging
import json
import os
from typing import Any
from uuid import uuid4

try:
    from airflow.models.baseoperator import BaseOperator
    from airflow.models.connection import Connection as AirflowConnection
except:
    class BaseOperator:
        template_fields = []


class TreasuryOrderUnload(BaseOperator):
    template_fields = list(BaseOperator.template_fields) + [
        'start_dttm',
        'end_dttm',
        'filename',
        'temp_dir',
    ]
    ui_color = '#161031'
    ui_fgcolor = '#de7900'
    do_xcom_push = True

    def __init__(
            self,
            *args,
            treasury_conn_id,
            temp_dir,
            filename=None,
            start_dttm=None,
            end_dttm=None,
            **kwargs):
        log = logging.getLogger(__name__)
        log.info('treasury unload operator: %s', kwargs['task_id'])
        super().__init__(*args, **kwargs)
        self.treasury_conn_id = treasury_conn_id
        self.filename = None
        self.api = None
        self.start_dttm = start_dttm
        self.end_dttm = end_dttm
        self.temp_dir = temp_dir
        self.filename = filename

    def output_filename(self):
        if self.filename:
            return os.path.join(self.temp_dir, self.filename)
        return os.path.join(self.temp_dir, uuid4().hex)

    def get_orders(self, output_filename, context):
        from .hooks import TreasuryHook
        hook = TreasuryHook(self.treasury_conn_id)
        self.log.info('looking for orders created between %s => %s', self.start_dttm, self.end_dttm)
        r1 = hook.api.orders_by_creation_date(self.start_dttm, self.end_dttm)
        self.log.info('looking for orders modified between %s => %s', self.start_dttm, self.end_dttm)
        r2 = hook.api.orders_by_modified_date(self.start_dttm, self.end_dttm)
        rg = []
        order_numbers = set()
        for x in chain(r1, r2):
            order_number = x['orderNo']
            if order_number not in order_numbers:
                order_numbers.add(order_number)
                rg.append(x)
        self.log.info('loaded %s orders', len(rg))
        with open(output_filename, 'w') as f:
            for x in rg:
                json.dump(x, f)
                f.write('\n')
        self.log.info('output filename: %s', output_filename)

    def execute(self, context) -> Any:
        output_filename = self.output_filename()
        self.get_orders(self.start_dttm, self.end_dttm)
        return output_filename


class TreasuryCouponUnload(BaseOperator):
    template_fields = list(BaseOperator.template_fields) + [
        'start_dttm',
        'end_dttm',
        'filename',
        'temp_dir',
    ]
    ui_color = '#161031'
    ui_fgcolor = '#de7900'
    do_xcom_push = True

    def __init__(
            self,
            *args,
            treasury_conn_id,
            temp_dir,
            filename=None,
            start_dttm=None,
            end_dttm=None,
            **kwargs):
        log = logging.getLogger(__name__)
        log.info('treasury unload operator: %s', kwargs['task_id'])
        super().__init__(*args, **kwargs)
        self.treasury_conn_id = treasury_conn_id
        self.filename = None
        self.api = None
        self.start_dttm = start_dttm
        self.end_dttm = end_dttm
        self.temp_dir = temp_dir
        self.filename = filename

    def output_filename(self):
        if self.filename:
            return os.path.join(self.temp_dir, self.filename)
        return os.path.join(self.temp_dir, uuid4().hex)

    def get_coupons(self, output_filename, context):
        from .hooks import TreasuryHook
        hook = TreasuryHook(self.treasury_conn_id)
        rg = list(hook.api.get_coupons())
        self.log.info('loaded %s coupons', len(rg))
        with open(output_filename, 'w') as f:
            for x in rg:
                json.dump(x, f)
                f.write('\n')
        self.log.info('output filename: %s', output_filename)

    def execute(self, context) -> Any:
        output_filename = self.output_filename()
        self.get_coupons(self.start_dttm, self.end_dttm)
        return output_filename
