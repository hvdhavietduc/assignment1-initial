#2012987
#Hà Việt Đức
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_case_100(self):
        """Testcase 100 """
        input =	"""a: float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 100))
    def test_case_101(self):
        """Testcase 101 """
        input =	"""a: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))
    def test_case_102(self):
        """Testcase 102 """
        input =	"""a: integer = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 102))
    def test_case_103(self):
        """Testcase 103 """
        input =	"""a: integer = 10.0;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 103))
    def test_case_104(self):
        """Testcase 104 """
        input =	"""a: integer = "str";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 104))
    def test_case_105(self):
        """Testcase 105 """
        input =	"""a: integer = b;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 105))
    def test_case_106(self):
        """Testcase 106 """
        input =	"""a: boolean = foo(1);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 106))
    def test_case_107(self):
        """Testcase 107 """
        input =	"""a: boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 107))
    def test_case_108(self):
        """Testcase 108 """
        input =	"""a, b: boolean = 1, 2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 108))
    def test_case_109(self):
        """Testcase 109 """
        input =	"""a: boolean = x + 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 109))
    #----------------------------------------------------------------------------------
     #----------------------------------------------------------------------------------
    def test_case_110(self):
        """Testcase 110 """
        input =	"""a: integer;
                   a, b: boolean = 1, 2;
                   c: string;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 110))
    def test_case_111(self):
        """Testcase 111 """
        input =	"""a: integer;
                   
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 111))
    def test_case_112(self):
        """Testcase 112 """
        input =	"""a: integer = 1;
            main: function void(){
                while( a==0 ){
                    x = f(2);
                    if(x==3){
                        break;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 112))
    def test_case_113(self):
        """Testcase 113 """
        input =	"""a: integer = 10.0;
            main: function void(){
                if(a>5){
                    x = a +5;
                }
                else {
                    x = a +6;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 113))
    def test_case_114(self):
        """Testcase 114 """
        input =	"""a: integer = "str";
            main: function void(){
                   do {
                      a = a+1;
                      x = foo(2,3+4);
                      printf(a);
                   } 
                   while(a==0);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 114))
    def test_case_115(self):
        """Testcase 115 """
        input =	"""a: integer = b;
                   a: function float(x: integer){
                        x = x+1;
                        return x;
                   } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 115))
    def test_case_116(self):
        """Testcase 116 """
        input =	"""a: boolean = foo(1);
                   a: function integer(){
                        return 5;
                   } 
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 116))
    def test_case_117(self):
        """Testcase 117 """
        input =	"""arr: array [2, 3] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 117))
    def test_case_118(self):
        """Testcase 118 """
        input =	"""arr: array [2, 3] of float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 118))
    def test_case_119(self):
        """Testcase 119 """
        input =	"""a: boolean = x + 1;
                    func: function integer(){
                        do {
                            a = a+1;
                            x = foo(2,3+4);
                            printf(a);
                            if(a>5){
                                x = a +5;
                            }
                            else {
                                x = a +6;
                            }

                        } 
                        while(a==0);
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 119))

        #-----------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------
    def test_case_120(self):
        """ Testcase 120 """
        input =	"""a: boolean = x + 1;
                    func: function integer(){
                        do {
                            a = a+1;
                            x = foo(2,3+4);
                            printf(a);
                            if(a>5){
                                x = a +5;
                            }
                            else {
                                x = a +6;
                            }

                        } 
                        while(a==0);
                    }
                    main: function auto(a: integer, arr: array [2, 3] of float){
                        return 1;
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 120))
    def test_case_121(self):
        """Testcase 121 """
        input =	"""a: boolean = x + 1;
                    func: function integer(){
                        do {
                            a = a+1;
                            x = foo(2,3+4);
                            printf(a);
                            if(a>5){
                                x = a +5;
                            }
                            else {
                                x = a +6;
                            }

                        } 
                        while(a==0);
                    }
                    main: function auto(a: integer, arr: array [2, 3] of float){
                        arr[1+1] = a;
                        return a[2];
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 121))
    def test_case_122(self):
        """Testcase 122 """
        input =	"""a: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                        }
                        while (a < 10) {
                            a = a + 1;
                        }

                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 122))
    def test_case_123(self):
        """Testcase 123 """
        input =	"""a: integer = 10.0;
            main: function void(){
                for(i=0,i<3,i+1){
                    a= a+1;
                }
            }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 123))
    def test_case_124(self):
        """Testcase 124 """
        input =	"""aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                            if(a>5){
                                break;
                            }
                            else{
                                continue;
                            }
                        }
                        while (a < 10) {
                            a = a + 1;
                        }

                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 124))
    def test_case_125(self):
        """Testcase 125 """
        input =	""" aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else if (result == 5) {
                            printf("The result is equal to 5.");
                        } else {
                            printf("The result is less than 5.");
                        }
                        for (i = 0, i < 3, i + 1) {
                            a = a + 1;
                            if (a > 5) {
                                break;
                            } else {
                                continue;
                            }
                        }
                        printf("The final value of a is %d.", a);
                        while (a < 10) {
                            a = a + 1;
                            if (a % 2 == 0) {
                                printf("%d is even.", a);
                            } else {
                                printf("%d is odd.", a);
                            }
                            for (j = 0, j < 3,  j + 1) {
                                arr[a % 2, j] = a + j;
                            }
                        }
                        printf("The final value of a is %d.", a);
                        printf("The final value of arr is:");
                        for (i = 0, i < 2, i + 1) {
                            for (j = 0, j < 3,  j + 1) {
                                printf("%d ", arr[i, j]);
                            }
                            printf("\\n");
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 125))
    def test_case_126(self):
        """Testcase 126 """
        input =	"""a: boolean = foo(1);
                main: function void() {
                    for (i = 0, i < 5,  i + 1) {
                        for (j = 0, j < 3, j + 1) {
                            arr[i, j] = func(i, j);
                        }
                    }
                    for (i = 0, i < 2,  i + 1) {
                        for (j = 0, j < 3,  j + 1) {
                            printf("%d ", arr[i, j]);
                        }
                        printf("\\n");
                    }
                    a: integer = 1;
                    while (a < 10) {
                        a = a + 1;
                        if (a % 2 == 0) {
                            continue;
                        }
                        printf("%d\\n", a);
                        for (i = 0, i < a, i + 1) {
                            if (i % 2 == 0) {
                                arr[0, i] = func(a, i);
                            } else {
                                arr[1, i] = func(a, i);
                            }
                        }
                        for (i = 0, i < 2, i + 1) {
                            for (j = 0, j < a,  j + 1) {
                                printf("%d ", arr[i, j]);
                            }
                            printf("\\n");
                        }
                        printf("\\n");
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 126))
    def test_case_127(self):
        """Testcase 127 """
        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 127))
    def test_case_128(self):
        """Testcase 128 """
        input =	"""sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to calculate the factorial of 5.
            factorial: integer = 1;
            while (i < 5) {
                i = i + 1;
                factorial = factorial * i;
            }
            printf("The factorial of 5 is %d\\n", factorial);

            // Use a do-while loop to read a number from the user and determine if it is positive.
            num: integer;
            do {
                printf("Enter a positive number: ");
                scanf("%d", num);
            } while (num <= 0);
            printf("You entered %d, which is positive.\\n", num);

            // Use a for loop to calculate the sum of the odd numbers from 1 to 100.
            odd_sum: integer = 0;
            for (i = 1, i <= 100,  i + 2) {
                odd_sum = sum(odd_sum, i);
            }
            printf("The sum of the odd numbers from 1 to 100 is %d\\n", odd_sum);

            // Use an if statement to determine if b is greater than or equal to 2.0 and less than or equal to 3.0.
            if ((b >= 2.0) &&( b <= 3.0)) {
                printf("b is between 2.0 and 3.0, inclusive.\\n");
            } else {
                printf("b is not between 2.0 and 3.0, inclusive.\\n");
            }

            // Use a nested for loop to calculate the product of the even elements of d.
            even_product: float = 1.0;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    if (d[i] % 2 == 0) {
                        even_product = prod(even_product, d[i]);
                    }
                }
            }
            printf("The product of the even elements of d is %.2f\\n", even_product);

            // Use a function call to calculate the sum of a and the result of the prod function.
            result: float = sum(a, prod(2.0, 3.5));
            printf("The sum of a and the product of 2.0 and 3.5 is %.2f\\n", result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 128))
    def test_case_129(self):
        """Testcase 129 """
        input =	"""a: integer = 1;
                    b: integer = 2;

                    // Define a function to compute the greatest common divisor (GCD) of two integers.
                    gcd: function auto(x: integer, y: integer) {
                        while (y != 0) {
                            r: integer = x % y;
                            x = y;
                            y = r;
                        }
                        return x;
                    }

                    main: function void() {
                        // Calculate the GCD of a and b using the gcd function.
                        g: integer = gcd(a, b);
                        printf("The GCD of %d and %d is %d.\\n", a, b, g);

                        // Use a for loop to calculate the sum of the first 100 integers.
                        s: integer = 0;
                        for (i = 1, i <= 100, i + 1) {
                            s = s + i;
                        }
                        printf("The sum of the first 100 integers is %d.\\n", s);

                        // Use assignments and function calls to compute the value of the expression (a + b) * (a - b) / (a * b).
                        p: integer = a + b;
                        q: integer = a - b;
                        r: integer = a * b;
                        result: float = (p * q) / r;
                        printf("The value of (a + b) * (a - b) / (a * b) is %.2f.\\n", result);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 129))
    #----------------------------------------------------------------------------------
     #----------------------------------------------------------------------------------
    def test_case_130(self):
        """Testcase 130 """
        input =	"""// Declare and initialize variables.
                    n: integer = 100;
                    sum: integer = 0;
                    prod: integer = 1;
                    count: integer = 0;

                    // Define a function to check if a number is prime.
                    is_prime: function auto(x: integer) {
                        if (x < 2) {
                            return false;
                        } else {
                            for (i = 2, i <= x / 2,  i + 1) {
                                if (x % i == 0) {
                                    return false;
                                }
                            }
                            return true;
                        }
                    }

                    // Define a function to compute the factorial of a number.
                    factorial: function auto(x: integer) {
                        if (x == 0) {
                            return 1;
                        } else {
                            return x * factorial(x - 1);
                        }
                    }

                    main: function void() {
                        // Use a while loop to calculate the sum of the first n odd integers.
                        i: integer = 1;
                        while (i <= n) {
                            sum = sum + i;
                            i = i + 2;
                        }
                        printf("The sum of the first %d odd integers is %d.\\n", n, sum);

                        // Use a for loop to calculate the product of the first n even integers that are not divisible by 3.
                        for (i = 2, count < n, i + 2) {
                            if (i % 3 != 0) {
                                prod = prod * i;
                                count = count + 1;
                            }
                        }
                        printf("The product of the first %d even integers not divisible by 3 is %d.\\n", n, prod);

                        // Use assignments and function calls to compute the value of the expression (n choose 2) * factorial(n - 2) / 2^n.
                        p: integer = factorial(n) / (factorial(2) * factorial(n - 2));
                        q: integer = 2 * n;
                        result: float = p * factorial(n - 2) / q;
                        printf("The value of (n choose 2) * factorial(n - 2) / 2^n is %.2f.\\n", result);

                        // Check if the number n is prime using the is_prime function.
                        if (is_prime(n)) {
                            printf("%d is prime.\\n", n);
                        } else {
                            printf("%d is not prime.\\n", n);
                        }
                    }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 130))
    def test_case_131(self):
        """Testcase 131 """
        input =	"""n: integer = 10;
                    a: float = 1.0;
                    b: float = 1.0;
                    sum: float = 0.0;
                main: function void(){
                    // Use a while loop to calculate the sum of the first n terms of the Fibonacci sequence.
                    i: integer = 1;
                    while (i <= n) {
                        if (i == 1) {
                            sum = a;
                        } else if (i == 2) {
                            sum = b;
                        } else {
                            sum = a + b;
                            a = b;
                            b = sum;
                        }
                        i = i + 1;
                    }
                    printf("The sum of the first %d terms of the Fibonacci sequence is %.2f.\\n", n, sum);

                    // Use a for loop to calculate the product of the first n positive integers.
                    prod: integer = 1;
                    for (i = 1, i <= n,  i + 1) {
                        prod = prod * i;
                    }
                    printf("The product of the first %d positive integers is %d.\\n", n, prod);

                    // Use an if statement to check if the number n is prime.
                    is_prime: boolean = true;
                    if (n < 2) {
                        is_prime = false;
                    } else {
                        for (i = 2,i <= n / 2, i + 1) {
                            if (n % i == 0) {
                                is_prime = false;
                                break;
                            }
                        }
                    }
                    if (is_prime) {
                        printf("%d is prime.\\n", n);
                    } else {
                        printf("%d is not prime.\\n", n);
                    }
                    }
                   
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 131))
    def test_case_132(self):
        """Testcase 132 """
        input =	"""// Define a function to calculate the factorial of a number.
                factorial: function auto(n: integer) {
                    if (n < 0) {
                        return -1;
                    } else if (n == 0) {
                        return 1;
                    } else {
                        fact: integer = 1;
                        i: integer = 1;
                        while (i <= n) {
                            fact = fact * i;
                            i = i + 1;
                        }
                        return fact;
                    }
                }

                // Declare and initialize variables.
                x: integer = 5;
                y: float = 2.0;
                result: float = 0.0;
                main: function void(){
                    // Calculate the result using a while loop and the factorial function.
                    i: integer = 0;
                    while (i <= x) {
                        if (i % 2 == 0) {
                            result = result + (y / factorial(i));
                        } else {
                            result = result - (y / factorial(i));
                        }
                        i = i + 1;
                    }
                

                // Output the result.
                printf("The result of the series is %.2f.\\n", result);
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 132))
    def test_case_133(self):
        """Testcase 133 """
        input =	"""// Define a function to calculate the nth Fibonacci number.
                    fibonacci: function auto(n: integer) {
                        if (n < 0) {
                            return -1;
                        } else if ((n == 0 )|| (n == 1)) {
                            return n;
                        } else {
                            return fibonacci(n-1) + fibonacci(n-2);
                        }
                    }

                    // Define a function to find the largest number in an array.
                    find_largest: function auto(arr: array [10] of integer) {
                        largest: integer = arr[0];
                        for (i = 1, i < 10, i+ 1) {
                            if (arr[i] > largest) {
                                largest = arr[i];
                            }
                        }
                        return largest;
                    }

                    // Define a function to find the sum of the elements in a row of a matrix.
                    row_sum: function auto(matrix: array [3, 3] of integer, row: integer) {
                        sum: integer = 0;
                        for (i = 0,i < 3, i + 1) {
                            sum = sum + matrix[row, i];
                        }
                        return sum;
                    }
                    main: function void(){
                        // Declare and initialize variables.
                        fib_nums: array [10] of integer;
                        for (i = 0, i < 10, i + 1) {
                            fib_nums[i] = fibonacci(i);
                        }

                        matrix: array [3, 3] of integer;

                        // Find the largest Fibonacci number.
                        largest_fib: integer = find_largest(fib_nums);

                        // Find the row with the largest sum in the matrix.
                        largest_sum: integer = 0;
                        largest_sum_row: integer = -1;
                        for (i = 0, i < 3,i + 1) {
                            sum = row_sum(matrix, i);
                            if (sum > largest_sum) {
                                largest_sum = sum;
                                largest_sum_row = i;
                            }
                        }

                    // Output the results.
                    printf("The largest Fibonacci number is %d.\\n", largest_fib);
                    printf("The row with the largest sum in the matrix is row %d, with a sum of %d.\\n", largest_sum_row, largest_sum);
                    }
                            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 133))
    def test_case_134(self):
        """Testcase 134 """
        input =	"""a: float = 1.0;
                b: float = -5.0;
                c: float = 6.0;
                delta: float = b * b - 4 * a * c;
                x1: float;
                x2: float;
                main: function void(){
                    if (delta > 0) {
                        x1 = (-b + sqrt(delta)) / (2 * a);
                        x2 = (-b - sqrt(delta)) / (2 * a);
                        printf("The equation has two real roots: %.2f and %.2f\\n", x1, x2);
                    } else if (delta == 0) {
                        x1 = -b / (2 * a);
                        printf("The equation has one real root: %.2f\\n", x1);
                    } else {
                        real_part: float = -b / (2 * a);
                        imaginary_part: float = sqrt(-delta) / (2 * a);
                        printf("The equation has two complex roots: %.2f + %.2fi and %.2f - %.2fi\\n", real_part, imaginary_part, real_part, imaginary_part);
                    }
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 134))
    def test_case_135(self):
        """Testcase 135 """
        input =	"""// Function to calculate the factorial of a positive integer
                     factorial: function integer(n: integer) {
                        if ((n == 0 )|| (n == 1)) {
                            return 1;
                        } else {
                            return n * factorial(n - 1);
                        }
                    }

                    // Function to calculate the nth Fibonacci number
                    fibonacci: function integer(n: integer) {
                        if ((n == 0) || (n == 1)) {
                            return n;
                        } else {
                            return fibonacci(n - 1) + fibonacci(n - 2);
                        }
                    }

                    // Function to calculate the sum of a geometric series
                     geometric_sum: function integer(a: float, r: float, n: integer) {
                        if (r == 1) {
                            return a * n;
                        } else {
                            return a * (1 - pow(r, n)) / (1 - r);
                        }
                    }

                    // Function to calculate the roots of a quadratic equation
                    quadratic_roots : function integer(a: float, b: float, c: float) {
                        delta: float = b * b - 4 * a * c;
                        x1: float;
                        x2: float;

                        if (delta > 0) {
                            x1 = (-b + sqrt(delta)) / (2 * a);
                            x2 = (-b - sqrt(delta)) / (2 * a);
                            printf("The equation has two real roots: %.2f and %.2f\\n", x1, x2);
                        } else if (delta == 0) {
                            x1 = -b / (2 * a);
                            printf("The equation has one real root: %.2f\\n", x1);
                        } else {
                            real_part: float = -b / (2 * a);
                            imaginary_part: float = sqrt(-delta) / (2 * a);
                            printf("The equation has two complex roots: %.2f + %.2fi and %.2f - %.2fi\\n", real_part, imaginary_part, real_part, imaginary_part);
                        }
                    }

                    // Main function
                    main: function void() {
                        // Calculate the factorial of 5
                        printf("The factorial of 5 is: %d\\n", factorial(5));

                        // Calculate the 10th Fibonacci number
                        printf("The 10th Fibonacci number is: %d\\n", fibonacci(10));

                        // Calculate the sum of the first 5 terms of the geometric series with a = 1 and r = 2
                        printf("The sum of the first 5 terms of the geometric series with a = 1 and r = 2 is: %.2f\\n", geometric_sum(1, 2, 5));

                        // Find the roots of the quadratic equation x^2 - 5x + 6 = 0
                        quadratic_roots(1, -5, 6);
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 135))
    def test_case_136(self):
        """Testcase 136 """
        input =	"""a: integer = 2;
                    b: integer = 5;
                    c: float = 3.14159;

                    func1: function auto(x: integer, y: integer) {
                        z: integer;
                        z = (x + y) * (x - y);
                        return z;
                    }

                    func2: function auto(x: float, y: float, z: float) {
                        a: float;
                        b: float;
                        c: float;
                        a = x * y * z;
                        b = x + y + z;
                        c = x / y;
                        return (a + b + c);
                    }

                    main: function void() {
                        result1: integer;
                        result2: float;
                        result1 = func1(a, b);
                        result2 = func2(c, result1, c);
                        if ((result1 > 10) && (result2 < 100)) {
                            printf("Both results are within the desired range.");
                        } else if (result1 > 10) {
                            printf("The first result is within the desired range, but the second is not.");
                        } else if (result2 < 100) {
                            printf("The second result is within the desired range, but the first is not.");
                        } else {
                            printf("Neither result is within the desired range.");
                        }
                        i: integer = 0;
                        while (i < 5) {
                            j: integer = i;
                            while (j < 5) {
                                printf("%d, %d\\n", i, j);
                                j = j + 1;
                            }
                            i = i + 1;
                        }
                    } 
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 136))
    def test_case_137(self):
        """Testcase 137 """
        input =	"""
                func1: function auto(x: integer, y: integer) {
                    z: integer;
                    z = (x + y) * (x - y);
                    return z;
                }

                func2: function auto(x: float, y: float) {
                    z: float;
                    z = x * y;
                    return z;
                }

                main: function void() {
                    result1: integer;
                    result2: float;
                    result1 = func1(a, c);
                    result2 = func2(b, d);
                    printf("The result of func1 is %d\\n", result1);
                    printf("The result of func2 is %.2f\\n", result2);
                    if (result1 % 2 == 0) {
                        printf("The result of func1 is even.\\n");
                    } else {
                        printf("The result of func1 is odd.\\n");
                    }
                    if ((result2 > 5) && (result2 < 10)) {
                        printf("The result of func2 is between 5 and 10.\\n");
                    } else {
                        printf("The result of func2 is not between 5 and 10.\\n");
                    }
                    i: integer = 0;
                    while (i < 5) {
                        j: integer = 0;
                        while (j < 5) {
                            if ((i + j == a) && (i * j == c)) {
                                printf("Found solution: i = %d, j = %d\\n", i, j);
                                break;
                            }
                            j = j + 1;
                        }
                        i = i + 1;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 137))
    def test_case_138(self):
        """Testcase 138 """
        input =	"""
                product: function auto(x: integer, y: integer) {
                    return x * y;
                }

                // Define a function to find the product of all numbers in an array
                productArray: function auto(numRows: integer, numCols: integer) {
                    result: integer = 1;
                    for (i = 0, i < numRows, i + 1) {
                        for (j = 0, j < numCols, j + 1) {
                            result = product(result, arr[i] );
                        }
                    }
                    return result;
                }
                bubbleSort: function void( numRows: integer, numCols: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }
                main: function void() {
                    // Define an array of 5 sub-arrays, each with 4 random integers between 1 and 10
                    arr: array [5, 4] of integer;
                    for (i = 0,i < 5, i + 1) {
                        for (j = 0, j < 4,j + 1) {
                            arr[i] = rand(1, 10);
                        }
                    }

                    // Print the array
                    printf("The array is:\\n");
                    for (i = 0, i < 5, i + 1) {
                        for (j = 0, j < 4, j + 1) {
                            printf("%d ", arr[i] );
                        }
                        printf("\\n");
                    }

                    // Find the sum of the second column
                    sum: integer = 0;
                    for (i = 0,i < 5,   i + 1) {
                        sum = sum + arr[i] ;
                    }
                    printf("The sum of the second column is %d.\\n", sum);

                    // Define a function to find the product of two numbers
                    

                    // Find the product of all numbers in the array
                    productAll: integer = productArray(arr, 5, 4);
                    printf("The product of all numbers in the array is %d.\\n", productAll);

                    // Define a function to sort an array in ascending order using bubble sort algorithm
                    

                    // Sort the array in ascending order
                    bubbleSort(arr, 5, 4);

                    // Print the sorted array
                    printf("The sorted array is:\\n");
                    for (i = 0, i < 5, i + 1) {
                        for (j = 0, j < 4,j + 1) {
                            printf("%d ", arr[i] );
                        }
                        printf("\\n");
                    }
                }

            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 138))
    def test_case_139(self):
        """Testcase 139 """
        input =	"""sum: integer = 0;
                i: integer = 0;
                count: integer = 0;
                main: function void(){
                    while (count < 50) {
                        if (i % 2 == 0) {
                            sum = sum+ i;
                            count = count+ 1;
                        }
                    i =i+ 1;
                    }

                    print("The sum of the first 50 even numbers is: " , sum);
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 139))
    def test_case_140(self):

        input = """a, b: array [3,2] of integer = {1,2,3 }, {1,2,3 };"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 140))
    
    def testParser37(self):
        """Empty program"""
        input_str = """"""
        expected = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input_str, expected, 141))

    def testParser39(self):
        """Call function outside function"""
        input_str = """
        printString("hello");
        }"""
        expect = "Error on line 2 col 8: printString"
        self.assertTrue(TestParser.test(input_str, expect, 142))

    def testParser40(self):
        """For outside function"""
        input_str = """
            for (i = 0, i < 10, i + 1) {
                printString("hello");
            }
        """
        expect = "Error on line 2 col 12: for"
        self.assertTrue(TestParser.test(input_str, expect, 143))

    def testParser41(self):
        """If outside function"""
        input_str = """
            if (a > 10) {
                printString("hello");
            }
        """
        expect = "Error on line 2 col 12: if"
        self.assertTrue(TestParser.test(input_str, expect, 144))

    def testParser42(self):
        """While outside function"""
        input_str = """
            while (a > 10) {
                printString("hello");
            }
        """
        expect = "Error on line 2 col 12: while"
        self.assertTrue(TestParser.test(input_str, expect, 145))

    

    def testParser49(self):
        input_str = """main: function void () {};"""
        expected = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.test(input_str, expected, 146))

    def testParser50(self):
        input_str = """
        main: function void () {
            if (x > 0) {
                printString("x is positive!");
        }
        """
        expected = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input_str, expected, 147))

    
    def testParser7(self):
        """Testing variable declaration with initial values:"""
        input_str = """
            program: function void () {
                a: integer = 10;
                b: float = 3.14e-7;
                c: boolean = true;
                d , e : array[2] of integer = {1, 2}, {3, 4}, {2,1};
            }
        """
        expect = "Error on line 6 col 60: ,"
        self.assertTrue(TestParser.test(input_str, expect, 148))

    

    def testParser21(self):
        input = """
        // Assert that comment is not parsed
        /* Assert that comment is not parsed */
        main: function array[1] of boolean (cd: auto, temp: string) {
            a=c[d[e[s["string"]]]];
            b=b[1,2,,3];
            return b;
        }"""
        expect = "Error on line 6 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 149))

    def testParser22(self):
        input = """
        program: function void (arr: array [10] of integer, left: integer, right: integer) {
            if (left < right) {
                mid = (left + right)/2;
                sort(arr, left, mid);
                sort(arr, mid + 1, right);
                merge(arr, left, mid, right);
            }
        }

        merge: function void (arr: array [10] of integer, left: integer, mid: integer, right: integer) {
            n1 = mid - left + 1;
            n2 = right - mid;

            left_arr : array [10] of integer;
            right_arr : array [10] of integer;

            for (i = 0, i < n1, i + 1) {
                left_arr[i] = arr[left + i];
            }
            for (j = 0, j < n2, j + 1) {
                right_arr[j] = arr[mid + 1 + j];
            }

            i = 0;
            j = 0;
            k = left;

            while ((i < n1) && (j < n2)) {
                if (left_arr[i] <= right_arr[j]) {
                    arr[k] = left_arr[i];
                    i = i + 1;
                }
                else {
                    arr[k] = right_arr[j];
                    j = j + 1;
                }
                k = k + 1;
            }

            while (i < n1) {
                arr[k] = left_arr[i];
                i = i + 1;
                k = k + 1;
            }

            while (j < n2) {
                arr[k] = right_arr[j];
                j = j + 1;
                k = k + 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 150))
    def test_case_151(self):
        input = """
        program: function void (arr: array [10] of integer, left: integer, right: integer) {
            if (left < right) {
                mid = (left + right)/2;
                sort(arr, left, mid);
                sort(arr, mid + 1, right);
                merge(arr, left, mid, right);
            }
        }

        merge: function void (arr: array [10] of integer, left: integer, mid: integer, right: integer) {
            n1 = mid - left + 1;
            n2 = right - mid;

            left_arr : array [10] of integer;
            right_arr : array [10] of integer;

            for (i = 0, i < n1, i + 1) {
                left_arr[i] = arr[left + i];
            }
            for (j = 0, j < n2, j + 1) {
                right_arr[j] = arr[mid + 1 + j];
            }

            i = 0;
            j = 0;
            k = left;

            while ((i < n1) && (j < n2)) {
                if (left_arr[i] <= right_arr[j]) {
                    arr[k] = left_arr[i];
                    i = i + 1;
                }
                else {
                    arr[k] = right_arr[j];
                    j = j + 1;
                }
                k = k + 1;
            }

            while (i < n1 && i +1) {
                arr[k] = left_arr[i];
                i = i + 1;
                k = k + 1;
            }

            while (j < n2) {
                arr[k] = right_arr[j];
                j = j + 1;
                k = k + 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 151))
    def test_case_152(self):
        input = """a, b: array [3,2] of integer = {1, 2, 3};"""
        expect = "Error on line 1 col 40: ;"
        self.assertTrue(TestParser.test(input, expect, 152))
    def test_case_153(self):
        input = """a, b: array [3,2] of integer = 1, 2, 3;"""
        expect = "Error on line 1 col 35: ,"
        self.assertTrue(TestParser.test(input, expect, 153))

    def test_case_154(self):
        input =	"""
                func1: function auto(x: integer, y: integer) {
                    z: integer;
                    z = (x + y) * (x - y);
                    return z;
                }

                func2: function auto(x: float, y: float) {
                    z: float;
                    z = x * y;
                    return z;
                }

                main: function void() {
                    result1: integer;
                    result2: float;
                    result1 = func1(a, c);
                    result2 = func2(b, d);
                    printf("The result of func1 is %d\\n", result1);
                    printf("The result of func2 is %.2f\\n", result2);
                    if (result1 % 2 == 0) {
                        printf("The result of func1 is even.\\n");
                    } else {
                        printf("The result of func1 is odd.\\n");
                    }
                    if ((result2 > 5) && (result2 < 10)) {
                        printf("The result of func2 is between 5 and 10.\\n");
                    } else {
                    }
                    i: integer = 0;
                    while (i < 5) {
                        j: integer = 0;
                        while (j < 5) {
                            if ((i + j == a) && (i * j == c)) {
                                printf("Found solution: i = %d, j = %d\\n", i, j);
                                break;
                            }
                            j = j + 1;
                        }
                        i = i + 1;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 154))
    def test_case_155(self):
        input =	"""n: integer = 10;
                    a: float = 1.0;
                    b: float = 1.0;
                    sum: float = 0.0;
                main: function void()
                    printf("The sum of the first %d terms of the Fibonacci sequence is %.2f.\\n", n, sum);

                    // Use a for loop to calculate the product of the first n positive integers.
                    prod: integer = 1;
                    for (i = 1, i <= n,  i + 1) {
                    }
                    printf("The product of the first %d positive integers is %d.\\n", n, prod);

                    // Use an if statement to check if the number n is prime.
                    is_prime: boolean = true;
                    if (n < 2) {
                        is_prime = false;
                    } else {
                        for (i = 2,i <= n / 2, i + 1) {
                            if (n % i == 0) {
                                is_prime = false;
                                break;
                            }
                        }
                    }
                    if (is_prime) {
                        printf("%d is prime.\\n", n);
                    } else {
                        printf("%d is not prime.\\n", n);
                    }
                    }
                   
        """
        expect = "Error on line 10 col 20: for"
        self.assertTrue(TestParser.test(input, expect, 155))
    def test_case_156(self):
        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0; i < 2;  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 43 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 156))
    def test_case_157(self):
        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while () {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 15 col 19: )"
        self.assertTrue(TestParser.test(input, expect, 157))
    def test_case_158(self):
        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i])
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 46 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 158))
    def test_case_159(self):
        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10,) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 29 col 32: )"
        self.assertTrue(TestParser.test(input, expect, 159))
    def test_case_160(self):
        input =	"""a: integer = 1;
                    b: integer = 2;

                    // Define a function to compute the greatest common divisor (GCD) of two integers.
                    gcd: function auto(x: integer, y: integer) {
                        while (y != 0) {
                            r: integer = x % y;
                            x = y;
                            y = r;
                        }
                        return x;
                    }

                    main: function void() {
                        // Calculate the GCD of a and b using the gcd function.
                        g: integer = gcd(a, b);
                        printf("The GCD of %d and %d is %d.\\n", a, b, g);

                        // Use a for loop to calculate the sum of the first 100 integers.
                        s: integer = 0;
                        for (i = 1, i <= 100, i + 1) {
                            s = s + i;
                        }
                        printf("The sum of the first 100 integers is %d.\\n", s);

                        // Use assignments and function calls to compute the value of the expression (a + b) * (a - b) / (a * b).
                        p: integer = a + b;
                        q: integer = a - b;
                        r: integer = a * b;
                        result: float = (p * q) / r;
                        printf("The value of (a + b) * (a - b) / (a * b) is %.2f.\\n", result);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 160))
    #--------------------------------------------------------------------------------
    def test_case_161(self):
        input =	"""a: integer = 1;
                    b: integer = 2;

                    // Define a function to compute the greatest common divisor (GCD) of two integers.
                    {
                        while (y != 0) {
                            r: integer = x % y;
                            x = y;
                            y = r;
                        }
                        return x;
                    }

                    main: function void() {
                        // Calculate the GCD of a and b using the gcd function.
                        g: integer = gcd(a, b);
                        printf("The GCD of %d and %d is %d.\\n", a, b, g);

                        // Use a for loop to calculate the sum of the first 100 integers.
                        s: integer = 0;
                        for (i = 1, i <= 100, i + 1) {
                            s = s + i;
                        }
                        printf("The sum of the first 100 integers is %d.\\n", s);

                        // Use assignments and function calls to compute the value of the expression (a + b) * (a - b) / (a * b).
                        p: integer = a + b;
                        q: integer = a - b;
                        r: integer = a * b;
                        result: float = (p * q) / r;
                        printf("The value of (a + b) * (a - b) / (a * b) is %.2f.\\n", result);
                    }"""
        expect = "Error on line 5 col 20: {"
        self.assertTrue(TestParser.test(input, expect, 161))
    def test_case_162(self):
        input =	"""a: integer = 1;
                    b: integer = 2

                    // Define a function to compute the greatest common divisor (GCD) of two integers.
                    gcd: function auto(x: integer, y: integer) {
                        while (y != 0) {
                            r: integer = x % y;
                            x = y;
                            y = r;
                        }
                        return x;
                    }

                    main: function void() {
                        // Calculate the GCD of a and b using the gcd function.
                        g: integer = gcd(a, b);
                        printf("The GCD of %d and %d is %d.\\n", a, b, g);

                        // Use a for loop to calculate the sum of the first 100 integers.
                        s: integer = 0;
                        for (i = 1, i <= 100, i + 1) {
                            s = s + i;
                        }
                        printf("The sum of the first 100 integers is %d.\\n", s);

                        // Use assignments and function calls to compute the value of the expression (a + b) * (a - b) / (a * b).
                        p: integer = a + b;
                        q: integer = a - b;
                        r: integer = a * b;
                        result: float = (p * q) / r;
                        printf("The value of (a + b) * (a - b) / (a * b) is %.2f.\\n", result);
                    }"""
        expect = "Error on line 5 col 20: gcd"
        self.assertTrue(TestParser.test(input, expect, 162))
    def test_case_163(self):
        input =	"""a: integer = 1;
                    b: integer = 2;

                    // Define a function to compute the greatest common divisor (GCD) of two integers.
                    gcd: function auto(x: integer, y: integer) {
                        while (y != 0) {
                            r: integer = x % y;
                            x = y;
                            y = r;
                        }
                        return x;
                    }

                    main: function void(int a) {
                        // Calculate the GCD of a and b using the gcd function.
                        g: integer = gcd(a, b);
                        printf("The GCD of %d and %d is %d.\\n", a, b, g);

                        // Use a for loop to calculate the sum of the first 100 integers.
                        s: integer = 0;
                        for (i = 1, i <= 100, i + 1) {
                            s = s + i;
                        }
                        printf("The sum of the first 100 integers is %d.\\n", s);

                        // Use assignments and function calls to compute the value of the expression (a + b) * (a - b) / (a * b).
                        p: integer = a + b;
                        q: integer = a - b;
                        r: integer = a * b;
                        result: float = (p * q) / r;
                        printf("The value of (a + b) * (a - b) / (a * b) is %.2f.\\n", result);
                    }"""
        expect = "Error on line 14 col 44: a"
        self.assertTrue(TestParser.test(input, expect, 163))

    def test_case_164(self):
        input =	"""a: integer = 1;
                    b: integer = 2;

                    // Define a function to compute the greatest common divisor (GCD) of two integers.
                    gcd: function auto(x, y: integer) {
                        while (y != 0) {
                            r: integer = x % y;
                            x = y;
                            y = r;
                        }
                        return x;
                    }

                    main: function void() {
                        // Calculate the GCD of a and b using the gcd function.
                        g: integer = gcd(a, b);
                        printf("The GCD of %d and %d is %d.\\n", a, b, g);

                        // Use a for loop to calculate the sum of the first 100 integers.
                        s: integer = 0;
                        for (i = 1, i <= 100, i + 1) {
                            s = s + i;
                        }
                        printf("The sum of the first 100 integers is %d.\\n", s);

                        // Use assignments and function calls to compute the value of the expression (a + b) * (a - b) / (a * b).
                        p: integer = a + b;
                        q: integer = a - b;
                        r: integer = a * b;
                        result: float = (p * q) / r;
                        printf("The value of (a + b) * (a - b) / (a * b) is %.2f.\\n", result);
                    }"""
        expect = "Error on line 5 col 40: ,"
        self.assertTrue(TestParser.test(input, expect, 164))
    def test_case_165(self):
        input =	"""aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                            if(a>5){
                                break;
                            }
                            else{
                                continue;
                            }
                        }
                        while (a < 10) {
                            a = a + 1;
                        

                    }"""
        expect = "Error on line 33 col 21: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 165))
    def test_case_166(self):
        input =	"""aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.")
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                            if(a>5){
                                break;
                            }
                            else{
                                continue;
                            }
                        }
                        while (a < 10) {
                            a = a + 1;
                        }

                    }"""
        expect = "Error on line 17 col 24: }"
        self.assertTrue(TestParser.test(input, expect, 166))
    def test_case_167(self):
        input =	"""aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                            if(a>5){
                                break;
                            }
                            else{
                                continue;
                            }
                        }
                        while (a < 10) {
                            a = a + 1;
                        }

                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 167))
    def test_case_168(self):
        input =	"""aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                            if(a>5){
                                break;
                            }
                            else{
                                continue;
                            }
                        }
                        while (a < 10 && a>1) {
                            a = a + 1;
                        }

                    }"""
        expect = "Error on line 29 col 42: >"
        self.assertTrue(TestParser.test(input, expect, 168))
    def test_case_169(self):
        input =	"""aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                            if(a>5){
                                break;
                            }
                            else{
                                continue;
                            }
                        }
                        while (a < 10) {
                            a = a + 1;
                        }

                    }"""
        expect = "Error on line 4 col 38: ;"
        self.assertTrue(TestParser.test(input, expect, 169))
    def test_case_170(self):

        input = """func: function integer () {
            printFloat("1+1");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 170))

    def test_case_171(self):

        input = """func: function array[] of float () {
          
               printFloat(12.1e45);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 171))

    def test_case_172(self):

        input = """func: function integer () {
           readFloat(1e10);
        }"""
        expect = "Error on line 2 col 21: 1e10"
        self.assertTrue(TestParser.test(input, expect, 172))

    def test_case_173(self):

        input = """func: function boolean () {
            readBoolean();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 173))
    def test_case_174(self):

        input = """
        func: function void ()
        {
        arr = {10.5, 20.3, 15.6, 18.9, 25.4};
        integer n = sizeof(arr) / sizeof(arr[0]);
         average = calculateAverage(arr, n);
        }
        """
        expect = "Error on line 5 col 8: integer"
        self.assertTrue(TestParser.test(input, expect, 174))

    def test_case_175(self):

        input = """func: function reverseString(str: string) {
            n = strlen(str);
            for (i = 0, i < n / 2, i + 1) {
                swap(str[i], str[n - i - 1]);
            }
        """
        expect = "Error on line 1 col 15: reverseString"
        self.assertTrue(TestParser.test(input, expect, 175))

    def test_case_176(self):

        input = """
                calculateExpApproximation(int n) {
            double result = 1.0;
            double term = 1.0;
            for (int i = 1; i <= n; i++) {
                term *= (1.0 / n);
                result += term;
            }
            return result;"""
        expect = "Error on line 2 col 41: ("
        self.assertTrue(TestParser.test(input, expect, 176))

    def test_case_177(self):

        input = """func: function float () {
            func();
            return expr;
        }

        c = expr;"""
        expect = "Error on line 6 col 10: ="
        self.assertTrue(TestParser.test(input, expect, 177))

    def test_case_178(self):

        input = """/* 
        double calculateExpression(int n) {
            double result = 0.0;
            for (int i = 1; i <= n; i++) {
                result += (double) i / (i + 1);
            }
            return result;*/
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 178))
    def test_case_179(self):

        input = """ func: int function fibonacci(n: int) {
                if (n == 0) {
                    return 0;
                } else if (n == 1) {
                    return 1;
                } else {
                    return fibonacci(n - 1) + fibonacci(n - 2);
                }
                }

                n: int = 10;
                result: int = fibonacci(n);

                print("The " + n + "th Fibonacci number is: " + result);       
        """
        expect = "Error on line 1 col 7: int"
        self.assertTrue(TestParser.test(input, expect, 179))
    def test_case_180(self):

        input = """ func: function integer (n: integer) {
                    if (n <= 1) {
                        return 0;
                    }
                    for (i = 2; i <= sqrt(n); i++) {
                        if (n % i == 0) {
                        return 0;
                        }
                    }
                    return 1;
                    }

                    func: int function largest_prime_factor(n: int) {
                    largest_factor: int = 0;
                    for (i = 2; i <= sqrt(n); i++) {
                        if (n % i == 0 && is_prime(i)) {
                        largest_factor = i;
                        }
                    }
                    if (largest_factor == 0) {
                        return n;
                    }
                    return largest_factor;
                    }

                    n: int = 123456789;
                    result: int = largest_prime_factor(n);

                    print("The largest prime factor of " + n + " is: " + result);  
        """
        expect = "Error on line 5 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 180))
    def test_case_181(self):

        input = """a = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
       """
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 181))
    def test_case_182(self):

        input = """/* 
        double calculateExpression(int n) {
            double result = 0.0;
            for (int i = 1; i <= n; i++) {
                result += (double) i / (i + 1);
            }
            return result;*/
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 182))
    def test_case_183(self):

        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 10 col 8: function"
        self.assertTrue(TestParser.test(input, expect, 183))
    def test_case_184(self):

        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0 ; i < 2 ;  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 43 col 23: ;"
        self.assertTrue(TestParser.test(input, expect, 184))
    def test_case_185(self):

        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0)

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 28 col 12: total"
        self.assertTrue(TestParser.test(input, expect, 185))
    def test_case_186(self):

        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer assign sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 51 col 28: assign"
        self.assertTrue(TestParser.test(input, expect, 186))
    def test_case_187(self):

        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x ++;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 3 col 22: +"
        self.assertTrue(TestParser.test(input, expect, 187))
    def test_case_188(self):

        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j++) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect = "Error on line 44 col 38: +"
        self.assertTrue(TestParser.test(input, expect, 188))
    def test_case_189(self):

        input = """product: function auto(x: int, y: integer) {
                    return x * y;
                }

                // Define a function to find the product of all numbers in an array
                productArray: function auto(numRows: integer, numCols: integer) {
                    result: integer = 1;
                    for (i = 0, i < numRows, i + 1) {
                        for (j = 0, j < numCols, j + 1) {
                            result = product(result, arr[i] );
                        }
                    }
                    return result;
                }
                bubbleSort: function void( numRows: integer, numCols: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }"""
        expect= "Error on line 1 col 26: int"
        self.assertTrue(TestParser.test(input, expect, 189))
    def test_case_190(self):

        input = """product: function auto(x: integer, y: integer) {
                    return x * y;
                }

                // Define a function to find the product of all numbers in an array
                productArray: function auto(numRows: integer, numCols: integer) {
                    result: integer = 1;
                    for (i = 0, i < numRows, i + 1) {
                        for (j = 0, j < numCols, j + 1) {
                            result = product(result, arr[i] );
                        }
                    }
                    return result;
                }
                bubbleSort: function void( numRows: integer, numCols: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k][i]  = arr[k][i] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }"""
        expect="Error on line 22 col 46: ["
        self.assertTrue(TestParser.test(input, expect, 190))
    def test_case_191(self):

        input = """product: function auto(x: integer, y: integer) {
                    return x ** y;
                }

                // Define a function to find the product of all numbers in an array
                productArray: function auto(numRows: integer, numCols: integer) {
                    result: integer = 1;
                    for (i = 0, i < numRows, i + 1) {
                        for (j = 0, j < numCols, j + 1) {
                            result = product(result, arr[i] );
                        }
                    }
                    return result;
                }
                bubbleSort: function void( numRows: integer, numCols: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }"""
        expect="Error on line 2 col 30: *"
        self.assertTrue(TestParser.test(input, expect, 191))
    def test_case_192(self):

        input = """product: function auto(x: integer, y: integer) {
                    return x * y;
                }

                // Define a function to find the product of all numbers in an array
                productArray: function auto(numRows: integer, numCols: integer) {
                    result: integer = 1;
                    for (i = 0, i < numRows, i + 1) {
                        for (j = 0, j < numCols, j + 1) {
                            result = product(result, arr[i] );
                        }
                    }
                    return result;
                }
                bubbleSort: function void( numRows: integer, numCols: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k == 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }"""
        expect="Error on line 20 col 43: =="
        self.assertTrue(TestParser.test(input, expect, 192))
    def test_case_193(self):

        input = """product: function auto(x: integer, y: integer) {
                    return x * y;
                }

                // Define a function to find the product of all numbers in an array
                productArray: function auto(numRows: integer, numCols: integer) {
                    result: integer = 1;
                    for (i = 0, i < numRows, i + 1) {
                        for (j = 0, j < numCols, j + 1) {
                            result = product(result, arr[i] );
                        }
                    }
                    return result;
                }
                bubbleSort: function void( numRows: integer, array: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }"""
        expect="Error on line 15 col 61: array"
        self.assertTrue(TestParser.test(input, expect, 193))
    def test_case_194(self):

        input = """java: float = !!a && b - "love" / "you";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 194))
    def test_case_195(self):

        input = """Array: array[3] of float = XYT[31, 12, 2002];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 195))
    def test_case_196(self):

        input = """      1bubbleSort: function void( numRows: integer, array: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }  
        """
        expect = "Error on line 1 col 6: 1"
        self.assertTrue(TestParser.test(input, expect, 196))
    def test_case_197(self):

        input = """   bubbleSort: function void( numRows: integer,Wrray: integer) {
                        for (i = 0, i < numRows && 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }     
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 197))
    def test_case_198(self):

        input = """      bubbleSort: function void( numRows: integer, irray: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    /* swap
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }  
        """
        expect = "Error on line 5 col 36: /"
        self.assertTrue(TestParser.test(input, expect, 198))
    def test_case_199(self):

        input = """ foo: function integer () {
            printFloat(12.e45);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 199))
