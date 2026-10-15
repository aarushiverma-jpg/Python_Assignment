company_data = {
    "departments": {
        "engineering": {
            "teams": {
                "backend": {
                    "manager": "Alice",
                    "budget": 150000,
                    "engineers": [
                        {"name": "Bob", "level": "Senior"},
                        {"name": "Charlie", "level": "Junior"}
                    ]
                },
                "frontend": {
                    "manager": "David",
                    "budget": 120000,
                    "engineers": []
                }
            }
        }
    },
    "location": "HQ"
}

backend_engineers=company_data.get('departments',{}).get('engineering',{}).get('teams',{}).get('backend',{}).get('engineers',{})

frontend_manager=company_data.get('departments',{}).get('engineering',{}).get('teams',{}).get('frontend',{}).get('manger','Unknown')
print("Backend engineers are: ")
for d in backend_engineers:
    for key,value in d.items():
        print(f"{key} : {value}",end="  ")
    print()
    
print(f"\nFrontend manager is : {frontend_manager}")