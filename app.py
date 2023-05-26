import requests
from bs4 import BeautifulSoup
from jinja2 import Template

def fetch_services(topmate_profile):
    # Step 2: Fetch all the services using Python
    try:
        response = requests.get(topmate_profile)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            service_elements = soup.select('.service')
            services = [elem.text.strip() for elem in service_elements]
            return services
        else:
            print(f"Error fetching services. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching services: {e}")
    
    return []

def build_page(services):
    # Step 3: Build a new page to display all the services
    with open('services.html') as file:
        template_content = file.read()
    
    template = Template(template_content)
    rendered_html = template.render(services=services)
    
    with open('output.html', 'w') as file:
        file.write(rendered_html)
    
    print("Page built successfully. Please check 'output.html' file.")

if __name__ == '__main__':
    # Step 1: Retrieve the input Topmate profile
    topmate_profile = input("Enter Topmate profile: ")
    
    # Fetch the services
    services = fetch_services(topmate_profile)
    
    # Build the HTML page to display the services
    build_page(services)
