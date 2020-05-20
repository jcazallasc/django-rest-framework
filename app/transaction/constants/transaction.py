import operator
from django.utils.translation import ugettext_lazy as _


TYPE_INFLOW = 'inflow'
TYPE_OUTFLOW = 'outflow'

VALID_TYPES = {
    TYPE_INFLOW: {
        'amount': {
            'operator': operator.ge,
            'value': 0,
            'error': _('Amount must be greater or equal than {}')
        },
    },
    TYPE_OUTFLOW: {
        'amount': {
            'operator': operator.lt,
            'value': 0,
            'error': _('Amount must be less than {}')
        },
    },
}
