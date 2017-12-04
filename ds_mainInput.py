from ds_add_mul import adder, multiplier
from ds_algo_input import algo_input
from ds_algorithm import algo
from ds_output import out

def main_input():
    input_var = raw_input("Enter the variable names:\t")
    input_varnum = len(input_var.strip())
    total_size = 0
    size = []
    for i in xrange(input_varnum):
        size.append(input("Enter the size of " + str(input_var[i])+"\t\t"))
        total_size += size[i]
    input_exp = raw_input("Enter the Boolean Expression:\t")

    exp_new = input_exp.split("+")


    exp_mul = []
    for term in exp_new:
        term = term.strip()
        var = {}
        for i in term:
            var[i] = []
            for j in xrange(size[input_var.find(i)]):
                var[i].append(i+str(j))
        #print var

        t = var[term[0]]
        for i in term[1:]:
            t = multiplier(t,var[i])
        exp_mul.append(t)



    exp_final = exp_mul[0]
    for i in exp_mul[1:]:
        exp_final  = adder(exp_final,i)

    print "Stage 1.1 - Expression Generation"
    print exp_final ,'\n'*10

    var = []
    for i in range(len(input_var)):
        for j in range(size[i]):
            var.append(input_var[i]+str(j))

    algos_input = []
    for i in exp_final:
        e= algo_input(var,i)
        if e == ['x'* total_size]:
            e.append(i)
        algos_input.append(e)

    
    print "Stage 1.2 - Cube generation from expression"
    print algos_input ,'\n'*10


    output_exp = []

    for i in range(len(algos_input)):
        if 'x'*total_size in algos_input[i]:
            output_exp.append(algos_input[i])
            #print i,algos_input[i]
        else:
            #print i,algo(algos_input[i])
            output_exp.append(algo(algos_input[i]))

    print "Stage 2 - Minimisation of expression (cubes)"
    print output_exp ,'\n'*10

    print "Stage 3 - Verilog File generation"
    out(input_var,output_exp,size,total_size)

main_input()
