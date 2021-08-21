# types for model Column
NAME = 'full_name'
JOB = 'job'
EMAIL = 'email'
DOMAIN = 'domain_name'
PHONE = 'phone_number'
COMPANY = 'company_name'
TEXT = 'text'
INT = 'integer'
ADDR = 'address'
DATE = 'date'

TYPES = (
    (NAME, 'Full name'),
    (JOB, 'Job'),
    (EMAIL, 'E-mail'),
    (DOMAIN, 'Domain name'),
    (PHONE, 'Phone number'),
    (COMPANY, 'Company name'),
    (TEXT, 'Text'),
    (INT, 'Integer'),
    (ADDR, 'Address'),
    (DATE, 'Date')
)

# column separators for model Schema
COM = ','
SEM = ';'
TAB = '\t'
SPC = ' '
DASH = '-'
PIPE = '|'

SEPARATORS = (
    (COM, 'Comma (,)'),
    (SEM, 'Semicolon (;)'),
    (TAB, 'Tab (\\t)'),
    (SPC, 'Space ( )'),
    (DASH, 'Dash (-)'),
    (PIPE, 'Pipes (|)')
)

# string characters for model Schema
DBL = '"'
SNGL = "'"

QUOTATION_CHARACTERS = (
    (DBL, 'Double-quote (")'),
    (SNGL, 'Single-quote (\')'),
)

# status for model Job
PROCESSING = "PROCESSING"
READY = "READY"
ERROR = "ERROR"

JOB_STATUS = (
    (PROCESSING, 'Processing'),
    (READY, 'Ready'),
    (ERROR, 'Error')
)
