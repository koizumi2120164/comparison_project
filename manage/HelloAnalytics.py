"""Hello Analytics Reporting API V4."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
import json
import re
import datetime


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'manage/json/comparisonproject-369302-d5be4cad2468.json'
VIEW_ID = '280731815'


def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '90daysAgo', 'endDate': 'Today'}],
          'metrics': [{'expression': 'ga:pageviews'}],
          'dimensions': [{'name': 'ga:pagePath'}]
        }]
      }
  ).execute()


def calc(response):
    """Calculate page views of each page path.

    Args:
        response: The Analytics Reporting API V4 response.
    """
    calc_res = dict()
    pv_summary = []
    report = response.get('reports', [])[0]
    dt_now = str(datetime.datetime.now())
    for report_data in report.get('data', {}).get('rows', []):
        # get page path
        page_path = report_data.get('dimensions', [])[0]
        # ignore query parameters
        page_path = re.sub(r'\?.+$', '', page_path)

        # get page view
        page_view = int(report_data.get('metrics', [])[0].get('values')[0])

        if page_path in calc_res:
            calc_res[page_path] += page_view
        else:
            calc_res[page_path] = page_view

    for path in calc_res:
        pv_summary.append({
            'page_path': path,
            'page_views': calc_res[path],
            'input_date': dt_now,
        })

    # sort by page views
    pv_summary.sort(
        key=lambda path_data: path_data['page_views'], reverse=True)

    return pv_summary


def save_as_json(data, file_path='./res.json'):
    """ Save dict pr list as JSON file.

    Args:
        data: dict or list object to save.
        file_path: file path for JSON file. (default is './res.json')
    """

    with open(file_path, 'w') as f:
        f.write(json.dumps(data, indent=2))


def main():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    summary = calc(response)
    save_as_json(summary, 'manage/json/summary.json')


if __name__ == '__main__':
    main()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(main, 'interval', minutes=5)
    scheduler.start()