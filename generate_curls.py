import subprocess

# 1. loginuser
cmd = 'curl -X POST -H "Content-Type: application/json" -d "{\\"userName\\": \\"admin\\", \\"password\\": \\"Admin@1234\\"}" http://127.0.0.1:8000/djangoapp/login'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('loginuser', 'w') as f:
    f.write('curl -X POST -H "Content-Type: application/json" -d \'{"userName": "admin", "password": "Admin@1234"}\' http://127.0.0.1:8000/djangoapp/login\n\nOutput:\n' + out)

# 2. logoutuser
cmd = 'curl http://127.0.0.1:8000/djangoapp/logout'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('logoutuser', 'w') as f:
    f.write('curl http://127.0.0.1:8000/djangoapp/logout\n\nOutput:\n' + out)

# 3. getalldealers
cmd = 'curl http://127.0.0.1:8000/djangoapp/get_dealers'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('getalldealers', 'w') as f:
    f.write('curl http://127.0.0.1:8000/djangoapp/get_dealers\n\nOutput:\n' + out)

# 4. getdealerbyid
cmd = 'curl http://127.0.0.1:8000/djangoapp/dealer/1'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('getdealerbyid', 'w') as f:
    f.write('curl http://127.0.0.1:8000/djangoapp/dealer/1\n\nOutput:\n' + out)

# 5. getdealersbyState
cmd = 'curl http://127.0.0.1:8000/djangoapp/get_dealers/Kansas'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('getdealersbyState', 'w') as f:
    f.write('curl http://127.0.0.1:8000/djangoapp/get_dealers/Kansas\n\nOutput:\n' + out)

# 6. getdealerreviews
cmd = 'curl http://127.0.0.1:8000/djangoapp/reviews/dealer/1'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('getdealerreviews', 'w') as f:
    f.write('curl http://127.0.0.1:8000/djangoapp/reviews/dealer/1\n\nOutput:\n' + out)

# 7. getallcarmakes
cmd = 'curl http://127.0.0.1:8000/djangoapp/get_cars'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('getallcarmakes', 'w') as f:
    f.write('curl http://127.0.0.1:8000/djangoapp/get_cars\n\nOutput:\n' + out)

# 8. analyzereview
cmd = 'curl http://127.0.0.1:5050/analyze/Fantastic%20services'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')
with open('analyzereview', 'w') as f:
    f.write('curl http://127.0.0.1:5050/analyze/Fantastic%20services\n\nOutput:\n' + out)

print('All cURL submission files generated successfully!')
