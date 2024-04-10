from repositories import customer_repository


def get_all_customers(db):
    customers = customer_repository.get_customers(db)
    # for customer in customers:
    #     print(customer)
    #     services = customer.servicios

    #     customer.servicios = services.split(',')
    return customers
