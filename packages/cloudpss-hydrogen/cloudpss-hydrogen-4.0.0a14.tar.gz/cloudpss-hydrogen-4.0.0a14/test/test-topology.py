import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import cloudpss
import time
import numpy as np
import pandas as pd
import json

if __name__ == '__main__':
    os.environ['CLOUDPSS_API_URL'] = 'http://cloudpss-calculate.local.ddns.cloudpss.net/'
    print('CLOUDPSS connected')
    cloudpss.setToken(
        'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInNjb3BlcyI6WyJtb2RlbDo5ODM2NyIsImZ1bmN0aW9uOjk4MzY3IiwiYXBwbGljYXRpb246MzI4MzEiXSwicm9sZXMiOlsiYWRtaW4iXSwidHlwZSI6ImFwcGx5IiwiZXhwIjoxNzQ5NzE2MzczLCJub3RlIjoiYWQiLCJpYXQiOjE3MTg2MTIzNzN9.XyaWizYSeT-AQAdndukdbUrS38DcWL4z85kIzBZCpAjwyCKbFVqX68xZGpkM8Pr5IX0yUHnZT93KNWJVpCXVAA')
    print('Token done')
    project = cloudpss.Model.fetch('model/CloudPSS/IEEE39')
    print(project.revision.hash)
    t = time.time()
    # topology = cloudpss.ModelTopology.fetch("hlbBPYIyQHWzgPxdjp9lV9a92twyxA2zETzrqz4Q0fou7mfOemX-pr9OfO9eUfq4","emtp",{'args':{}})
    # topology = cloudpss.ModelTopology.fetch("JwHbZdjco9eC0nZw3fY7Iz9rqsQ4HFGJObiBW3bFuYLPCd0Vqb2vb8zNY28D1AXV","emtp",{'args':{}})
    print(time.time()-t)
    
    runner = project.run()
    while not runner.status():
        logs = runner.result.getLogs()
        for log in logs:
            print(log)
    logs = runner.result.getLogs()
    for log in logs:
        print(log)     

    # topology= project.fetchTopology(config={'args':{}},maximumDepth=10)

    # topology.dump(topology,'test.json')
    
    
    