from enum import StrEnum

# These are only the High Contrast versions, which tend to look better (imo)
# the normal variants are 30-37
# theres a lot more codes: `man 4 console_codes`

class ANSIColor(StrEnum):
    """ANSI color codes for terminal output."""
    RESET   = '\033[0m'
    BLACK   = '\033[90m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    PURPLE  = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'

class ANSIBackgroundColor(StrEnum):
    """ANSI background color codes for terminal output."""
    RESET   = '\033[0m'
    BLACK   = '\033[100m'
    RED     = '\033[101m'
    GREEN   = '\033[102m'
    YELLOW  = '\033[103m'
    BLUE    = '\033[104m'
    PURPLE  = '\033[105m'
    CYAN    = '\033[106m'
    WHITE   = '\033[107m'

class NoColor(ANSIColor):
    """No-op color codes for plain text output."""
    RESET   = ''
    BLACK   = ''
    RED     = ''
    GREEN   = ''
    YELLOW  = ''
    BLUE    = ''
    PURPLE  = ''
    CYAN    = ''
    WHITE   = ''
