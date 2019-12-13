import requests
import json
from requests.auth import HTTPBasicAuth

# can be moved to config files to decouple
api_url = 'http://34.70.250.255//artifactory/api/{}'
username = 'admin'
password = 'X4HDz9PYEq'


def get_maven_artifacts():
    """
    Gets list of all artifacts for maven repository
    Args: None
    Returns: returns list of artifacts for a specified repository
    """
    data = 'items.find({"repo":{"$eq":"jcenter-cache"}})'
    results = []
    try:
        r = requests.post(url=api_url.format('search/aql/'), data=data, auth=HTTPBasicAuth(username, password))
        results = json.loads(r.content)['results']
    except Exception as e:
        print (e)
    return results


def get_file_stats_for_artifacts():
    """
    Gets the file stats that include download count for every artifact in the list of artifacts for maven repository
    Args: None
    Returns: Returns list of file stats with download count > 0
    """
    artifacts = get_maven_artifacts()
    download_list = []
    for item in artifacts:
        new_url = api_url.format('storage/{}?stats'.format(item['repo'] + '/' + item['path'] + '/' + item['name']))
        try:
            resp = requests.get(url=new_url, auth=HTTPBasicAuth(username, password), timeout=5)
            content = json.loads(resp.content)
        except Exception as e:
            print (e)
            continue
        if content['downloadCount'] > 0:
            download_list.append(content)
    return download_list


def get_most_popular_artifacts(artifacts_list):
    """
    Takes filtered artifacts_list as input and sorts them based on downloadCount
    Args: artifacts_list (list)
    Returns: top 2 artifacts with highest downloadCount
    """
    sorted_list = sorted(artifacts_list, key=lambda i: (i.get('downloadCount')), reverse=True)
    return sorted_list[0], sorted_list[1]


def main():
    filtered_list = get_file_stats_for_artifacts()
    first, second = get_most_popular_artifacts(filtered_list)
    return first, second


if __name__ == "__main__":
    main()
