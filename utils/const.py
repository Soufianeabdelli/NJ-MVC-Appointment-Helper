
MVC_URL = 'https://telegov.njportal.com/njmvc/AppointmentWizard/'
PRJ_URL = 'https://github.com/tangbao/NJ-MVC-Appointment-Helper/'
LOCATION_LIST_URL = 'https://github.com/tangbao/NJ-MVC-Appointment-Helper/blob/master/location_list.md'

SERVICE_ID = {
    'INITIAL PERMIT (NOT FOR KNOWLEDGE TEST)': '15',
    'CDL PERMIT OR ENDORSEMENT - (NOT FOR KNOWLEDGE TEST)': '14',
    'REAL ID': '12',
    'NON-DRIVER ID': '16',
    'KNOWLEDGE TESTING': '17',
    'RENEWAL: LICENSE OR NON-DRIVER ID': '11',
    'RENEWAL: CDL': '6',
    'TRANSFER FROM OUT OF STATE': '7',
    'NEW TITLE OR REGISTRATION': '8',
    'SENIOR NEW TITLE OR REGISTRATION (65+)': '9',
    'REGISTRATION RENEWAL': '10',
    'TITLE DUPLICATE/REPLACEMENT': '13'
}

SERVICE_KEYBOARD = [['INITIAL PERMIT (NOT FOR KNOWLEDGE TEST)', 'KNOWLEDGE TESTING', 'REAL ID'],
                    ['CDL PERMIT OR ENDORSEMENT - (NOT FOR KNOWLEDGE TEST)', 'NON-DRIVER ID'],
                    ['RENEWAL: LICENSE OR NON-DRIVER ID', 'RENEWAL: CDL', 'TRANSFER FROM OUT OF STATE'],
                    ['NEW TITLE OR REGISTRATION', 'SENIOR NEW TITLE OR REGISTRATION (65+)'],
                    ['REGISTRATION RENEWAL', 'TITLE DUPLICATE/REPLACEMENT']]

LOCATION_ID = {'186': 'Bakers Basin', '187': 'Bayonne', '189': 'Camden', '208': 'Cardiff', '191': 'Delanco',
               '192': 'Eatontown', '194': 'Edison', '195': 'Flemington', '197': 'Freehold', '198': 'Lodi',
               '200': 'Newark', '201': 'North Bergen', '203': 'Oakland', '204': 'Paterson', '206': 'Rahway',
               '207': 'Randolph', '188': 'Rio Grande', '190': 'Salem', '193': 'South Plainfield', '196': 'Toms River',
               '199': 'Vineland', '202': 'Wayne', '205': 'West Deptford', '163': 'Bakers Basin', '164': 'Bayonne',
               '166': 'Camden', '185': 'Cardiff', '168': 'Delanco', '169': 'Eatontown', '171': 'Edison',
               '172': 'Flemington', '174': 'Freehold', '175': 'Lodi', '177': 'Newark', '178': 'North Bergen',
               '180': 'Oakland', '181': 'Paterson', '183': 'Rahway', '184': 'Randolph', '165': 'Rio Grande',
               '167': 'Salem', '170': 'South Plainfield', '173': 'Toms River', '176': 'Vineland', '179': 'Wayne',
               '182': 'West Deptford', '124': 'Bakers Basin', '125': 'Bayonne', '127': 'Camden', '146': 'Cardiff ',
               '129': 'Delanco', '130': 'Eatontown', '132': 'Edison', '133': 'Flemington', '135': 'Freehold',
               '136': 'Lodi', '138': 'Newark', '139': 'North Bergen', '141': 'Oakland', '142': 'Paterson',
               '144': 'Rahway', '145': 'Randolph', '126': 'Rio Grande', '128': 'Salem', '131': 'South Plainfield',
               '134': 'Toms River', '137': 'Vineland', '140': 'Wayne', '143': 'West Deptford', '209': 'Bakers Basin',
               '210': 'Bayonne', '212': 'Camden', '231': 'Cardiff', '214': 'Delanco', '215': 'Eatontown',
               '217': 'Edison', '218': 'Flemington', '220': 'Freehold', '221': 'Lodi', '223': 'Newark',
               '224': 'North Bergen', '226': 'Oakland', '227': 'Paterson', '229': 'Rahway', '230': 'Randolph',
               '211': 'Rio Grande', '213': 'Salem', '216': 'South Plainfield', '219': 'Toms River', '222': 'Vineland',
               '225': 'Wayne', '228': 'West Deptford', '232': 'Bakers Basin', '233': 'Bayonne', '235': 'Camden',
               '254': 'Cardiff', '237': 'Delanco', '238': 'Eatontown', '240': 'Edison', '241': 'Flemington',
               '243': 'Freehold', '244': 'Lodi', '246': 'Newark', '247': 'North Bergen', '249': 'Oakland',
               '250': 'Paterson', '252': 'Rahway', '253': 'Randolph', '234': 'Rio Grande', '236': 'Salem',
               '239': 'South Plainfield', '242': 'Toms River', '245': 'Vineland', '248': 'Wayne',
               '251': 'West Deptford', '101': 'Bakers Basin', '102': 'Bayonne', '104': 'Camden', '105': 'Cardiff ',
               '107': 'Delanco', '108': 'Eatontown', '110': 'Edison', '111': 'Flemington', '113': 'Freehold',
               '114': 'Lodi', '116': 'Newark', '117': 'North Bergen', '119': 'Oakland', '120': 'Paterson',
               '122': 'Rahway', '123': 'Randolph', '103': 'Rio Grande', '106': 'Salem', '109': 'South Plainfield',
               '112': 'Toms River', '115': 'Vineland', '118': 'Wayne', '121': 'West Deptford', '7': 'Bakers Basin',
               '8': 'Bayonne', '10': 'Camden', '11': 'Cardiff', '13': 'Delanco', '14': 'Eatontown', '16': 'Edison',
               '17': 'Flemington', '19': 'Freehold', '20': 'Lodi', '22': 'Newark', '23': 'North Bergen',
               '25': 'Oakland', '26': 'Paterson', '28': 'Rahway', '29': 'Randolph', '9': 'Rio Grande', '12': 'Salem',
               '15': 'South Plainfield', '18': 'Toms River', '21': 'Vineland', '24': 'Wayne', '27': 'West Deptford',
               '46': 'Bakers Basin', '47': 'Bayonne', '49': 'Camden', '48': 'Cardiff', '50': 'Delanco',
               '51': 'Eatontown', '52': 'Edison', '53': 'Flemington', '54': 'Freehold', '55': 'Lodi', '56': 'Newark',
               '57': 'North Bergen', '58': 'Oakland', '59': 'Paterson', '60': 'Rahway', '61': 'Randolph',
               '62': 'Rio Grande', '64': 'Salem', '63': 'South Plainfield', '65': 'Toms River', '66': 'Vineland',
               '67': 'Wayne', '68': 'West Deptford', '30': 'Cherry Hill', '31': 'East Orange', '32': 'Hazlet',
               '33': 'Jersey City', '34': 'Lakewood', '35': 'Manahawkin', '36': 'Medford', '37': 'Newton',
               '256': 'Rio Grande', '38': 'Runnemede', '39': 'Somerville', '40': 'South Brunswick', '41': 'Springfield',
               '42': 'Trenton Regional', '43': 'Turnersville', '44': 'Wallington', '45': 'Washington',
               '79': 'Manahawkin', '71': 'Somerville', '85': 'Cherry Hill', '86': 'East Orange', '87': 'Hazlet',
               '88': 'Jersey City', '89': 'Lakewood', '90': 'Manahawkin', '91': 'Medford', '92': 'Newton',
               '257': 'Rio Grande', '93': 'Runnemede', '94': 'Somerville', '95': 'South Brunswick', '96': 'Springfield',
               '97': 'Trenton Regional', '98': 'Turnersville', '99': 'Wallington', '100': 'Washington',
               '147': 'Cherry Hill', '148': 'East Orange', '149': 'Hazlet', '150': 'Jersey City', '151': 'Lakewood',
               '152': 'Manahawkin', '153': 'Medford', '154': 'Newton', '255': 'Rio Grande', '155': 'Runnemede',
               '156': 'Somerville', '157': 'South Brunswick', '158': 'Springfield', '159': 'Trenton Regional',
               '160': 'Turnersville', '161': 'Wallington', '162': 'Washington', '0': 'All'}

LOCATION_ID_ADDR = {'186': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '187': 'RT 440 & 1347 Kennedy Blvd. , Family Dollar Plaza, Bayonne, NJ, 07002',
                    '189': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '208': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '191': '400 Creek Road, Delanco, NJ, 08075', '192': '109 Rt. 36, Eatontown, NJ, 07724',
                    '194': '45 Kilmer Road, Edison, NJ, 08817', '195': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '197': '811 Okerson Road, Freehold, NJ, 07728', '198': '8 Mill Street, Lodi, NJ, 07644',
                    '200': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '201': '8901 Park Plaza, 90th & Bergenline Avenue, North Bergen, NJ, 07047',
                    '203': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '204': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '206': '1140 Woodbridge Road, Rahway, NJ, 07065', '207': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '188': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '190': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '193': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '196': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '199': '9 West Park Avenue, Vineland, NJ, 08360', '202': '481 Route 46 West, Wayne, NJ, 07470',
                    '205': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '163': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '164': 'RT 440 & 1347 Kennedy Blvd. , Family Dollar Plaza, Bayonne, NJ, 07002',
                    '166': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '185': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '168': '400 Creek Road, Delanco, NJ, 08075', '169': '109 Rt. 36, Eatontown, NJ, 07724',
                    '171': '45 Kilmer Road, Edison, NJ, 08817', '172': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '174': '811 Okerson Road, Freehold, NJ, 07728', '175': '8 Mill Street, Lodi, NJ, 07644',
                    '177': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '178': '8901 Park Plaza, 90th & Bergenline Avenue, North Bergen, NJ, 07047',
                    '180': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '181': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '183': '1140 Woodbridge Road, Rahway, NJ, 07065', '184': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '165': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '167': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '170': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '173': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '176': '9 West Park Avenue, Vineland, NJ, 08360', '179': '481 Route 46 West, Wayne, NJ, 07470',
                    '182': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '124': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '125': 'RT 440 & 1347 Kennedy Blvd. , Family Dollar Plaza, Bayonne, NJ, 07002',
                    '127': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '146': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '129': '400 Creek Road, Delanco, NJ, 08075', '130': '109 Rt. 36, Eatontown, NJ, 07724',
                    '132': '45 Kilmer Road, Edison, NJ, 08817', '133': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '135': '811 Okerson Road, Freehold, NJ, 07728', '136': '8 Mill Street, Lodi, NJ, 07644',
                    '138': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '139': '8901 Park Plaza, 90th & Bergenline Avenue, North Bergen, NJ, 07047',
                    '141': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '142': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '144': '1140 Woodbridge Road, Rahway, NJ, 07065', '145': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '126': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '128': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '131': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '134': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '137': '9 West Park Avenue, Vineland, NJ, 08360', '140': '481 Route 46 West, Wayne, NJ, 07470',
                    '143': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '209': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '210': 'RT 440 & 1347 Kennedy Blvd. , Family Dollar Plaza, Bayonne, NJ, 07002',
                    '212': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '231': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '214': '400 Creek Road, Delanco, NJ, 08075', '215': '109 Rt. 36, Eatontown, NJ, 07724',
                    '217': '45 Kilmer Road, Edison, NJ, 08817', '218': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '220': '811 Okerson Road, Freehold, NJ, 07728', '221': '8 Mill Street, Lodi, NJ, 07644',
                    '223': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '224': '8901 Park Plaza, 90th & Bergenline Avenue, North Bergen, NJ, 07047',
                    '226': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '227': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '229': '1140 Woodbridge Road, Rahway, NJ, 07065', '230': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '211': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '213': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '216': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '219': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '222': '9 West Park Avenue, Vineland, NJ, 08360', '225': '481 Route 46 West, Wayne, NJ, 07470',
                    '228': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '232': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '233': 'RT 440 & 1347 Kennedy Blvd. , Family Dollar Plaza, Bayonne, NJ, 07002',
                    '235': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '254': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '237': '400 Creek Road, Delanco, NJ, 08075', '238': '109 Rt. 36, Eatontown, NJ, 07724',
                    '240': '45 Kilmer Road, Edison, NJ, 08817', '241': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '243': '811 Okerson Road, Freehold, NJ, 07728', '244': '8 Mill Street, Lodi, NJ, 07644',
                    '246': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '247': '8901 Park Plaza, 90th & Bergenline Avenue, North Bergen, NJ, 07047',
                    '249': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '250': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '252': '1140 Woodbridge Road, Rahway, NJ, 07065', '253': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '234': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '236': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '239': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '242': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '245': '9 West Park Avenue, Vineland, NJ, 08360', '248': '481 Route 46 West, Wayne, NJ, 07470',
                    '251': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '101': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '102': 'RT 440 & 1347 Kennedy Blvd, Family Dollar Plaza, Bayonne, NJ, 07002',
                    '104': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '105': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '107': '400 Creek Road, Delanco, NJ, 08075', '108': '109 Rt. 36, Eatontown, NJ, 07724',
                    '110': '45 Kilmer Road, Edison, NJ, 08817', '111': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '113': '811 Okerson Road, Freehold, NJ, 07728', '114': '8 Mill Street, Lodi, NJ, 07644',
                    '116': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '117': '8901 Park Plaza, 90th & Bergenline Avenue, North Bergen, NJ, 07047',
                    '119': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '120': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '122': '1140 Woodbridge Road, Rahway, NJ, 07065', '123': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '103': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '106': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '109': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '112': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '115': '9 West Park Avenue, Vineland, NJ, 08360', '118': '481 Route 46 West, Wayne, NJ, 07470',
                    '121': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '7': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '8': 'RT 440 & 1347 Kennedy Blvd., Family Dollar Plaza , Bayonne, NJ, 07002',
                    '10': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '11': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '13': '400 Creek Road, Delanco, NJ, 08075', '14': '109 Rt. 36, Eatontown, NJ, 07724',
                    '16': '45 Kilmer Road, Edison, NJ, 08817', '17': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '19': '811 Okerson Road, Freehold, NJ, 07728', '20': '8 Mill Street, Lodi, NJ, 07644',
                    '22': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '23': '8901 Park Plaza, 90th & Bergenline Avenue , North Bergen, NJ, 07047',
                    '25': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '26': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '28': '1140 Woodbridge Road, Rahway, NJ, 07065', '29': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '9': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '12': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '15': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '18': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '21': '9 West Park Avenue, Vineland, NJ, 08360', '24': '481 Route 46 West, Wayne, NJ, 07470',
                    '27': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '46': '3200 Brunswick Pike, Lawrenceville, NJ, 08648',
                    '47': 'RT 440 & 1347 Kennedy Blvd., Family Dollar Plaza , Bayonne, NJ, 07002',
                    '49': '2600 Mt. Ephraim Avenue, Camden, NJ, 08104',
                    '48': '6725 Black Horse Pike, Harbor Square, Egg Harbor Twp, NJ, 08234-3935',
                    '50': '400 Creek Road, Delanco, NJ, 08075', '51': '109 Rt. 36, Eatontown, NJ, 07724',
                    '52': '45 Kilmer Road, Edison, NJ, 08817', '53': '181 Routes 31 & 202 B, Flemington, NJ, 08551',
                    '54': '811 Okerson Road, Freehold, NJ, 07728', '55': '8 Mill Street, Lodi, NJ, 07644',
                    '56': '228 Frelinghuysen Avenue, Newark, NJ, 07114',
                    '57': '8901 Park Plaza, 90th & Bergenline Avenue , North Bergen, NJ, 07047',
                    '58': '350 Ramapo Valley Road, Suite 24, Oakland, NJ, 07436',
                    '59': '125 Broadway, Suite 201, Paterson, NJ, 07505',
                    '60': '1140 Woodbridge Road, Rahway, NJ, 07065', '61': '160 Canfield Avenue, Randolph, NJ, 07869',
                    '62': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '64': '199 East Broadway, Finlaw Building, Salem, NJ, 08079',
                    '63': '5000 Hadley Road, South Plainfield, NJ, 07080',
                    '65': '1861 Hooper Avenue, Village Square Plaza, Toms River, NJ, 08753',
                    '66': '9 West Park Avenue, Vineland, NJ, 08360', '67': '481 Route 46 West, Wayne, NJ, 07470',
                    '68': '215 Crown Point Road, Thorofare, NJ, 08086',
                    '30': '1 Executive Campus, Route 70 & Cuthbert Blvd, Suite 110, Cherry Hill, NJ, 08002',
                    '31': '183 South 18th Street, East Orange, NJ, 07018',
                    '32': '1374 Route 36, Airport Plaza Mall, Hazlet, NJ, 07730',
                    '33': '438 Summit Avenue, Jersey City, NJ, 07307',
                    '34': '1195 Route 70, Store 9, Leisure Center, Lakewood, NJ, 08701',
                    '35': '712 East Bay Avenue, Manahawkin Plaza, Manahawkin, NJ, 08050',
                    '36': "175 Route 70, Suite 25, Sharp's Run Plaza, Medford, NJ, 08055",
                    '37': '51 Sparta Avenue, Newton, NJ, 07860',
                    '256': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '38': '835 E. Clements Bridge Rd, Runnemede Plaza, Runnemede, NJ, 08078',
                    '39': '10 Roosevelt Place, Somerville, NJ, 08876', '40': '2236 Rt. 130 North, Dayton, NJ, 08810',
                    '41': '34 Center Street, Springfield, NJ, 07081',
                    '42': '120 South Stockton Street, Trenton, NJ, 08666',
                    '43': '5200 Route 42 North, Ganttown Plaza, Suite 13, Turnersville, NJ, 08012',
                    '44': '450 Main Avenue, Wallington Square, Wallington, NJ, 07057',
                    '45': '404 E Washington Ave, Washington, NJ, 07882',
                    '79': '712 East Bay Avenue, Manahawkin Plaza, Manahawkin, NJ, 08050',
                    '71': '10 Roosevelt Place, Somerville, NJ, 08876',
                    '85': '1 Executive Campus, Route 70 & Cuthbert Blvd, Suite 110, Cherry Hill, NJ, 08002',
                    '86': '183 South 18th Street, East Orange, NJ, 07018',
                    '87': '1374 Route 36, Airport Plaza Mall, Hazlet, NJ, 07730',
                    '88': '438 Summit Avenue, Jersey City, NJ, 07307',
                    '89': '1195 Route 70, Store 9, Leisure Center, Lakewood, NJ, 08701',
                    '90': '712 East Bay Avenue, Manahawkin Plaza, Manahawkin, NJ, 08050',
                    '91': "175 Route 70, Suite 25, Sharp's Run Plaza, Medford, NJ, 08055",
                    '92': '51 Sparta Avenue, Newton, NJ, 07860',
                    '257': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '93': '835 E. Clements Bridge Rd, Runnemede Plaza, Runnemede, NJ, 08078',
                    '94': '10 Roosevelt Place, Somerville, NJ, 08876', '95': '2236 Rt. 130 North, Dayton, NJ, 08810',
                    '96': '34 Center Street, Springfield, NJ, 07081',
                    '97': '120 South Stockton Street, Trenton, NJ, 08666',
                    '98': '5200 Route 42 North, Ganttown Plaza, Suite 13, Turnersville, NJ, 08012',
                    '99': '450 Main Avenue, Wallington Square, Wallington, NJ, 07057',
                    '100': '404 E Washington Ave, Washington, NJ, 07882',
                    '147': '1 Executive Campus, Route 70 & Cuthbert Blvd, Suite 110, Cherry Hill, NJ, 08002',
                    '148': '183 South 18th Street, East Orange, NJ, 07018',
                    '149': '1374 Route 36, Airport Plaza Mall, Hazlet, NJ, 07730',
                    '150': '438 Summit Avenue, Jersey City, NJ, 07307',
                    '151': '1195 Route 70, Store 9, Leisure Center, Lakewood, NJ, 08701',
                    '152': '712 East Bay Avenue, Manahawkin Plaza, Manahawkin, NJ, 08050',
                    '153': "175 Route 70, Suite 25, Sharp's Run Plaza, Medford, NJ, 08055",
                    '154': '51 Sparta Avenue, Newton, NJ, 07860',
                    '255': '3305 Bay Shore Road, Breakwater Shopping Plaza, North Cape May, NJ, 08204',
                    '155': '835 E. Clements Bridge Rd, Runnemede Plaza, Runnemede, NJ, 08078',
                    '156': '10 Roosevelt Place, Somerville, NJ, 08876', '157': '2236 Rt. 130 North, Dayton, NJ, 08810',
                    '158': '34 Center Street, Springfield, NJ, 07081',
                    '159': '120 South Stockton Street, Trenton, NJ, 08666',
                    '160': '5200 Route 42 North, Ganttown Plaza, Suite 13, Turnersville, NJ, 08012',
                    '161': '450 Main Avenue, Wallington Square, Wallington, NJ, 07057',
                    '162': '404 E Washington Ave, Washington, NJ, 07882'}

LOCATION_NAME = {'15': {'186': 'Bakers Basin', '187': 'Bayonne', '189': 'Camden', '208': 'Cardiff', '191': 'Delanco',
                        '192': 'Eatontown', '194': 'Edison', '195': 'Flemington', '197': 'Freehold', '198': 'Lodi',
                        '200': 'Newark', '201': 'North Bergen', '203': 'Oakland', '204': 'Paterson', '206': 'Rahway',
                        '207': 'Randolph', '188': 'Rio Grande', '190': 'Salem', '193': 'South Plainfield',
                        '196': 'Toms River', '199': 'Vineland', '202': 'Wayne', '205': 'West Deptford'},
                 '14': {'163': 'Bakers Basin', '164': 'Bayonne', '166': 'Camden', '185': 'Cardiff', '168': 'Delanco',
                        '169': 'Eatontown', '171': 'Edison', '172': 'Flemington', '174': 'Freehold', '175': 'Lodi',
                        '177': 'Newark', '178': 'North Bergen', '180': 'Oakland', '181': 'Paterson', '183': 'Rahway',
                        '184': 'Randolph', '165': 'Rio Grande', '167': 'Salem', '170': 'South Plainfield',
                        '173': 'Toms River', '176': 'Vineland', '179': 'Wayne', '182': 'West Deptford'},
                 '12': {'124': 'Bakers Basin', '125': 'Bayonne', '127': 'Camden', '146': 'Cardiff ', '129': 'Delanco',
                        '130': 'Eatontown', '132': 'Edison', '133': 'Flemington', '135': 'Freehold', '136': 'Lodi',
                        '138': 'Newark', '139': 'North Bergen', '141': 'Oakland', '142': 'Paterson', '144': 'Rahway',
                        '145': 'Randolph', '126': 'Rio Grande', '128': 'Salem', '131': 'South Plainfield',
                        '134': 'Toms River', '137': 'Vineland', '140': 'Wayne', '143': 'West Deptford'},
                 '16': {'209': 'Bakers Basin', '210': 'Bayonne', '212': 'Camden', '231': 'Cardiff', '214': 'Delanco',
                        '215': 'Eatontown', '217': 'Edison', '218': 'Flemington', '220': 'Freehold', '221': 'Lodi',
                        '223': 'Newark', '224': 'North Bergen', '226': 'Oakland', '227': 'Paterson', '229': 'Rahway',
                        '230': 'Randolph', '211': 'Rio Grande', '213': 'Salem', '216': 'South Plainfield',
                        '219': 'Toms River', '222': 'Vineland', '225': 'Wayne', '228': 'West Deptford'},
                 '17': {'232': 'Bakers Basin', '233': 'Bayonne', '235': 'Camden', '254': 'Cardiff', '237': 'Delanco',
                        '238': 'Eatontown', '240': 'Edison', '241': 'Flemington', '243': 'Freehold', '244': 'Lodi',
                        '246': 'Newark', '247': 'North Bergen', '249': 'Oakland', '250': 'Paterson', '252': 'Rahway',
                        '253': 'Randolph', '234': 'Rio Grande', '236': 'Salem', '239': 'South Plainfield',
                        '242': 'Toms River', '245': 'Vineland', '248': 'Wayne', '251': 'West Deptford'},
                 '11': {'101': 'Bakers Basin', '102': 'Bayonne', '104': 'Camden', '105': 'Cardiff ', '107': 'Delanco',
                        '108': 'Eatontown', '110': 'Edison', '111': 'Flemington', '113': 'Freehold', '114': 'Lodi',
                        '116': 'Newark', '117': 'North Bergen', '119': 'Oakland', '120': 'Paterson', '122': 'Rahway',
                        '123': 'Randolph', '103': 'Rio Grande', '106': 'Salem', '109': 'South Plainfield',
                        '112': 'Toms River', '115': 'Vineland', '118': 'Wayne', '121': 'West Deptford'},
                 '6': {'7': 'Bakers Basin', '8': 'Bayonne', '10': 'Camden', '11': 'Cardiff', '13': 'Delanco',
                       '14': 'Eatontown', '16': 'Edison', '17': 'Flemington', '19': 'Freehold', '20': 'Lodi',
                       '22': 'Newark', '23': 'North Bergen', '25': 'Oakland', '26': 'Paterson', '28': 'Rahway',
                       '29': 'Randolph', '9': 'Rio Grande', '12': 'Salem', '15': 'South Plainfield', '18': 'Toms River',
                       '21': 'Vineland', '24': 'Wayne', '27': 'West Deptford'},
                 '7': {'46': 'Bakers Basin', '47': 'Bayonne', '49': 'Camden', '48': 'Cardiff', '50': 'Delanco',
                       '51': 'Eatontown', '52': 'Edison', '53': 'Flemington', '54': 'Freehold', '55': 'Lodi',
                       '56': 'Newark', '57': 'North Bergen', '58': 'Oakland', '59': 'Paterson', '60': 'Rahway',
                       '61': 'Randolph', '62': 'Rio Grande', '64': 'Salem', '63': 'South Plainfield',
                       '65': 'Toms River', '66': 'Vineland', '67': 'Wayne', '68': 'West Deptford'},
                 '8': {'30': 'Cherry Hill', '31': 'East Orange', '32': 'Hazlet', '33': 'Jersey City', '34': 'Lakewood',
                       '35': 'Manahawkin', '36': 'Medford', '37': 'Newton', '256': 'Rio Grande', '38': 'Runnemede',
                       '39': 'Somerville', '40': 'South Brunswick', '41': 'Springfield', '42': 'Trenton Regional',
                       '43': 'Turnersville', '44': 'Wallington', '45': 'Washington'},
                 '9': {'79': 'Manahawkin', '71': 'Somerville'},
                 '10': {'85': 'Cherry Hill', '86': 'East Orange', '87': 'Hazlet', '88': 'Jersey City', '89': 'Lakewood',
                        '90': 'Manahawkin', '91': 'Medford', '92': 'Newton', '257': 'Rio Grande', '93': 'Runnemede',
                        '94': 'Somerville', '95': 'South Brunswick', '96': 'Springfield', '97': 'Trenton Regional',
                        '98': 'Turnersville', '99': 'Wallington', '100': 'Washington'},
                 '13': {'147': 'Cherry Hill', '148': 'East Orange', '149': 'Hazlet', '150': 'Jersey City',
                        '151': 'Lakewood', '152': 'Manahawkin', '153': 'Medford', '154': 'Newton', '255': 'Rio Grande',
                        '155': 'Runnemede', '156': 'Somerville', '157': 'South Brunswick', '158': 'Springfield',
                        '159': 'Trenton Regional', '160': 'Turnersville', '161': 'Wallington', '162': 'Washington'}}
