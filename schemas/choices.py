COM = 'comma'
SEM = 'semicolon'
TAB = 'tab'
SPC = 'space'
PIPE = 'pipe'
DBL = 'double-quote'
SNGL = 'single-quote'
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

SEPARATORS = (
    (COM, 'Comma (,)'),
    (SEM, 'Semicolon (;)'),
    (TAB, 'Tab (\\t)'),
    (SPC, 'Space ( )'),
    (PIPE, 'Pipe (|)')
)

QUOTATION_CHARACTERS = (
    (DBL, 'Double-quote (")'),
    (SNGL, 'Single-quote (\')'),
)