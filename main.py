import codecs
import datetime
from dateutil import rrule
import requests
import tabulate

import configuration as con


def week_diff(start, until):
    return rrule.rrule(rrule.WEEKLY, dtstart=start, until=until).count()


def calculate_passed_time():
    """Return passed week ratio and remaining weeks"""
    total = week_diff(
        datetime.date(*con.START_DATE),
        datetime.date(*con.RELEASE_DATE)
    )

    today = datetime.date.today()
    current = week_diff(datetime.date(*con.START_DATE), today)

    passed = float(current) / total
    remaining = total - current
    return passed, remaining


def magic(target, actual, passed):
    """Wanna some magics?"""

    target_to_date = int(passed * target)

    return [
        target,
        actual,
        target - actual,            # Actual remain
        target_to_date,
        target - target_to_date,    # Target to date remain
        target_to_date - actual,    # Actual to date remain
    ]


def create_table(data, headers):
    return tabulate.tabulate(
        data,
        headers=headers,
        tablefmt='pipe',    # For markdown format
        numalign='center',
        stralign='center'
    )


def create_output_string(team_table, member_table):
    return '\n\n'.join([
        '### Team target', team_table,
        '### Member target (commit/review)', member_table
    ])


def write_to_markdown(output_string, remaining_weeks):
    today = datetime.date.today().strftime('%Y%m%d')
    filename = con.MARKDOWN_FILE.format(remaining_weeks, today)
    with codecs.open(filename, mode='w', encoding='utf-8') as markdown:
        markdown.write(output_string)


def generate_data_table():
    passed, remaining_weeks = calculate_passed_time()
    team_rows = []
    member_rows = []

    team_commit = 0
    team_review = 0

    for index, member in enumerate(con.MEMBERS):
        url = con.CONTRIBUTION_API.format(con.CYCLE, member['user_id'])
        data = requests.get(url).json()['contribution']

        # Actual - We will not count workflow +1 | See sample response below
        actual_commit = data['commit_count']
        actual_review = sum(data['marks'][i] for i in ['-1', '-2', '1', '2'])

        magic_commit = magic(member['commit'], actual_commit, passed)
        magic_review = magic(member['review'], actual_review, passed)

        contexts = zip(magic_commit, magic_review)

        row = [index + 1, member['name']]
        for context in contexts:
            row.append('{}/{}'.format(*context))
        member_rows.append(row)

        team_commit += actual_commit
        team_review += actual_review

    member_table = create_table(member_rows, con.MEMBER_HEADERS)

    team_rows = [
        [1, 'Commits'] + magic(con.TEAM_TARGET['commit'], team_commit, passed),
        [2, 'Reviews'] + magic(con.TEAM_TARGET['review'], team_review, passed)
    ]
    team_table = create_table(team_rows, con.TEAM_HEADERS)

    return team_table, member_table


def main():
    team_table, member_table = generate_data_table()
    output_string = create_output_string(team_table, member_table)

    # Un-comment this if you do not want to print
    print(output_string)

    # Un-comment this if you want to write to file
    # write_to_markdown(output_string, remaining_weeks)


if __name__ == '__main__':
    main()
