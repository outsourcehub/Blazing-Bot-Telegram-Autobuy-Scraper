"""
Ultra-Fast Trading Bot Configuration
Contract Detection & Monitoring Only
"""
import os

def config(key, default=None, cast=None):
    """Simple config function to replace decouple"""
    value = os.environ.get(key, default)
    if cast and value is not None:
        try:
            return cast(value)
        except (ValueError, TypeError):
            return default
    return value

# Telegram Bot Configuration
BOT_TOKEN = config('BOT_TOKEN', default='YOUR_BOT_TOKEN_HERE')
API_ID = config('API_ID', default=0)
API_HASH = config('API_HASH', default='YOUR_API_HASH_HERE')
OWNER_CHAT_ID = config('OWNER_CHAT_ID', default=0, cast=int)

# Scraper User Authentication (for channel monitoring)
SCRAPER_PHONE = config('SCRAPER_PHONE', default='')
SCRAPER_PASSWORD = config('SCRAPER_PASSWORD', default='')

# DBOTX API Configuration
DBOTX_API_KEY = config('DBOTX_API_KEY', default='')
DBOTX_BASE_URL = 'https://api-data-v1.dbotx.com'

# Supabase Configuration (for verification monitoring)
SUPABASE_URL = config('SUPABASE_URL', default='https://ofririwzonwekmyqgqlg.supabase.co')
SUPABASE_ANON_KEY = config('SUPABASE_ANON_KEY', default='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mcmlyaXd6b253ZWtteXFncWxnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE0MDM1MzYsImV4cCI6MjA3Njk3OTUzNn0.1PQ9Fg4V04kaCZQm_7c88p65cOWboAs1htzjvQ_Tsko')
SUPABASE_SERVICE_KEY = config('SUPABASE_SERVICE_KEY', default='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mcmlyaXd6b253ZWtteXFncWxnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MTQwMzUzNiwiZXhwIjoyMDc2OTc5NTM2fQ.NoNkxXOnVDgSRw0KBnT0iyi25m6oCYmzKFWEfrh5z3Y')

# For backwards compatibility
SUPABASE_KEY = SUPABASE_ANON_KEY

# Supabase Table Names
VERIFY_REQUESTS_TABLE = 'verify_requests'
WALLET_PATTERNS_TABLE = 'wallet_patterns'
REALTIME_CHANNEL = 'verify_updates'

# Speed Optimization Settings
HTTP_TIMEOUT = 5.0
MAX_CONNECTIONS = 20
MAX_RETRIES = 3
CONCURRENT_LIMIT = 10

# Speed Mode - Skip delays for maximum speed
_speed_mode_val = config('SPEED_MODE', default='true')
SPEED_MODE = str(_speed_mode_val).lower() == 'true' if _speed_mode_val else True

# Delay settings (only used when SPEED_MODE=false)
_delay_min = config('HUMAN_DELAY_MIN', default='0.05')
_delay_max = config('HUMAN_DELAY_MAX', default='0.1')
HUMAN_DELAY_MIN = float(_delay_min) if _delay_min else 0.05
HUMAN_DELAY_MAX = float(_delay_max) if _delay_max else 0.1

# Session Configuration
SESSION_NAME = 'trading_bot_session'
WORKDIR = os.path.dirname(os.path.abspath(__file__))

# Chain Configuration - Only Enable/Disable Chains
DEFAULT_SETTINGS = {
    'enabled_chains': ['solana', 'bsc', 'ethereum', 'base', 'arbitrum', 'story', 'monad', 'sonic', 'avax', 'bera']
}

# RPC Endpoints for EVM Chain Detection
EVM_RPC_ENDPOINTS = {
    'base': 'https://base-rpc.publicnode.com',
    'bsc': 'https://bsc-rpc.publicnode.com',
    'ethereum': 'https://eth-rpc.publicnode.com',
    'story': 'https://story-evm-rpc.publicnode.com',
    'monad': 'https://monad-testnet-rpc.publicnode.com',
    'sonic': 'https://sonic-rpc.publicnode.com',
    'avax': 'https://avax-rpc.publicnode.com',
    'bera': 'https://berachain-rpc.publicnode.com'
}

# Blockchain Detection Patterns (Pre-compiled for speed)
CHAIN_PATTERNS = {
    'tron': r'^T[A-Za-z0-9]{33}$',
    'bsc': r'^0x[a-fA-F0-9]{40}$',
    'base': r'^0x[a-fA-F0-9]{40}$',
    'ethereum': r'^0x[a-fA-F0-9]{40}$',
    'arbitrum': r'^0x[a-fA-F0-9]{40}$',
    'story': r'^0x[a-fA-F0-9]{40}$',
    'monad': r'^0x[a-fA-F0-9]{40}$',
    'sonic': r'^0x[a-fA-F0-9]{40}$',
    'avax': r'^0x[a-fA-F0-9]{40}$',
    'bera': r'^0x[a-fA-F0-9]{40}$',
    'solana': r'^[1-9A-HJ-NP-Za-km-z]{32,44}$'
}

# Menu Configuration (Channel Management Only)
MENU_EMOJI = {
    'channels': '📡',
    'add_channel': '➕',
    'remove_channel': '🗑️',
    'toggle_channel': '🔄',
    'channel_settings': '⚙️',
    'filter_mode': '🔍',
    'active': '✅',
    'inactive': '❌',
    'all_msgs': '📢',
    'admin_only': '👑',
    'specific_users': '👥',
    'back': '⬅️',
    'save': '💾',
    'reset': '🔄',
}
