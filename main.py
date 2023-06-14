
import my_utils2 as mu2

if __name__ == '__main__':

    csv_file = 'numbers3.csv'
    print(mu2.find_roots(1, -1, -1))

    mu2.generate_csv(csv_file, 10)
    print(mu2.my_read_csv(csv_file))

#    @mu2.quadratic_equation_decorator
    mu2.find_roots(1,-1,1)