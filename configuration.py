# OpenStack current cycle information
CYCLE = 'rocky'                 # Cycle name/code
# Date format [YYYY, MM, DD] without any leading zero :))
START_DATE = [2018, 3, 5]       # First date of the cycle
RELEASE_DATE = [2018, 8, 31]    # Last date of the cycle

# Output markdown filename
MARKDOWN_FILE = 'fvl-contribution-rocky-{}-{}.md'

# URL to contribution API of Stackalytics
CONTRIBUTION_API = ('http://stackalytics.com/api/1.0/contribution?'
                    'release={}&company=fujitsu&user_id={}')

# Overall team target for commit/review
TEAM_TARGET = {
    'commit': 129,
    'review': 616,
}

# Member information and commit/review target for each member
MEMBERS = [
    # Format: user id, member name, target commit, target review
    {'user_id': 'kiennt2609', 'name': 'Kien', 'commit': 0, 'review': 0},
    {'user_id': 'daidv', 'name': 'Dai', 'commit': 0, 'review': 0},
    {'user_id': 'namnh', 'name': 'Nam', 'commit': 43, 'review': 205},
    {'user_id': 'duonghq', 'name': 'Duong', 'commit': 43, 'review': 205},
    {'user_id': 'tovin07', 'name': 'Vinh', 'commit': 43, 'review': 206},
]

# Table headers for team contribution summary
# See comment for the calculation
TEAM_HEADERS = [
    'No.',
    'Item',
    'Target',
    'Actual',
    'Actual remain',            # = Target - Actual
    'Target to date',           # = Target to date
    'Target to date remain',    # = Target - Target to date
    'Actual to date remain',    # = Target to date - Actual
]

# Table headers for detail team member's contribution
# See comment for the calculation
MEMBER_HEADERS = [
    'No.',
    'Member',
    'Target',
    'Actual',
    'Actual remain',            # = Target - Actual
    'Target to date',           # = Target to date
    'Target to date remain',    # = Target - Target to date
    'Actual to date remain',    # = Target to date - Actual
]
