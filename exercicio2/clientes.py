def read_clients_file(file):
    clients = []
    with open(file, 'r') as f:
        for line in f:
            name, city, age, salary = line.strip().split(';')
            clients.append({
                'name': name,
                'city': city,
                'age': int(age),
                'salary': float(salary)
            })
    return clients

def calc_avg(clients):
    total_age = sum(client['age'] for client in clients)
    total_salary = sum(client['salary'] for client in clients)
    avg_age = total_age / len(clients)
    avg_salary = total_salary / len(clients)
    return avg_age, avg_salary

if __name__ == "__main__":
    clients = read_clients_file('clientes.txt')
    avg_age, avg_salary = calc_avg(clients)
    
    print(f"Média de idade: {avg_age:.2f} anos")
    print(f"Média de renda mensal: R$ {avg_salary:.2f}")
