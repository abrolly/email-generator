import json
import random
import time
from pathlib import Path

import clipboard

path_to_file = Path(__file__).parent.resolve()

def main():
    print('Generating random email')

    with open(f'{path_to_file}/data.json') as f:
        data = json.load(f)

    fname = random.choice(data['fname'])
    lname = random.choice(data['lname'])
    timestamp = int(time.time())

    random_email = f'{fname}_{lname}_{timestamp}@globalization-partners.com' 

    print(f'Email generated: {random_email}')
    clipboard.copy(random_email)

if __name__ == '__main__':
    main()    
