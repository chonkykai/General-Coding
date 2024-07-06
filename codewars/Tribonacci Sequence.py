def tribonacci(signature, n):
    x,y,z = 0, 1, 2
    output = []
    if n == 0:
        return output
    elif n == 1:
        output = [signature[0]]
        return output
    elif n == 2:
        output = [signature[0],signature[1]]
        return output
    elif n == 3:
        return signature
    else:
        output = signature + []
        for i in range (3,n):
            summmation = output[x] + output[y] + output[z]
            output.append(summmation)
            x += 1
            y += 1
            z +=1
        return output