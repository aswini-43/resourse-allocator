print("enter 1or 2 or 3 \n1.minimum N CPUs for H hours\n 2. maximum price they are willing to pay for H hours \nor3 a combination of both.")
types=int(input())
hours=int(input())
us_east= { 
"large": 0.12, 
"xlarge": 0.23, 
"2xlarge": 0.45, 
"4xlarge": 0.774, 
"8xlarge": 1.4, 
"10xlarge": 2.82 
}
us_west= { 
"large": 0.14, 
"2xlarge": 0.413, 
"4xlarge": 0.89, 
"8xlarge": 1.3, 
"10xlarge": 2.97 
}

new_nodes_east=[]
count_east=[]
new_nodes_west=[]
count_west=[]
def server(new_nodes_east,count_east,counte,new_nodes_west,count_west,countw,price_east,price_west):
    servere=[]
    
    server=zip(new_nodes_east,count_east)
    servere=list(server)
    serverw=[]
    server=zip(new_nodes_west,count_west)
    serverw=list(server)
    result(price_east,price_west,servere,serverw) 
    
def result(price_east,price_west,servere,serverw):
    final=[]
    
    result={}
    result["Region"]="us-east"
    result["Total-cost$"]=round(price_east,2)
    result["servers"]=servere
    
    result_west={}
    result_west["Region"]="us-west"
    result_west["Total-cost $"]=round(price_west,2)
    result_west["servers"]=serverw
    
    final.append(result)
    final.append(result_west)
    print(final)

        
def type_one(cpus,hours,price_east,price_west,price,t):
    counte=0
    countw=0
    while(cpus!=0):
        cpu=cpus
        for i in us_east:
        
            if(cpus>=32):
                count_of_32_east=int(cpus/32)
                price_east+=count_of_32_east*us_east["10xlarge"]
                cpus=cpus-(count_of_32_east*32)
                new_nodes_east.append("10xlarge")
                count_east.append(count_of_32_east)
                counte+=1
            elif(cpus>=16 and cpus<32):
                count_of_16_east=int(cpus/16)
                price_east+=count_of_16_east*us_east["8xlarge"]
                cpus=cpus-(count_of_16_east*16)
                new_nodes_east.append("8xlarge")
                count_east.append(count_of_16_east)
                counte+=1
            elif(cpus>=8 and cpus<16):
                count_of_8_east=int(cpus/8)
                price_east+=count_of_8_east*us_east["4xlarge"]
                cpus=cpus-(count_of_8_east*8)
                new_nodes_east.append("4xlarge")
                count_east.append(count_of_8_east)
                counte+=1
            elif(cpus>=4 and cpus<8):
                count_of_4_east=int(cpus/4)
                price_east+=count_of_4_east*us_east["2xlarge"]
                cpus=cpus-(count_of_4_east*4)
                new_nodes_east.append("2xlarge")
                count_east.append(count_of_4_east)
                counte+=1
            elif(cpus>=2 and cpus<4):
                count_of_2_east=int(cpus/2)
                price_east+=count_of_2_east*us_east["xlarge"]
                cpus=cpus-(count_of_2_east*2)
                new_nodes_east.append("xlarge")
                count_east.append(count_of_2_east)
                counte+=1
            elif(cpus==1):
                
                count_of_1_east=int(cpus/1)
                price_east+=count_of_1_east*us_east["large"]
                
                cpus=cpus-(count_of_1_east*1)
                new_nodes_east.append("large")
                count_east.append(count_of_1_east)
                counte+=1
        cpus=cpu
    
    
        for j in us_west:
        
            if(cpus>=32):
                count_of_32_west=int(cpus/32)
                price_west+=count_of_32_west*us_west["10xlarge"]
                cpus=cpus-(count_of_32_west*32)
                new_nodes_west.append("10xlarge")
                count_west.append(count_of_32_west)
                countw+=1
            elif(cpus>=16 and cpus<32):
                count_of_16_west=int(cpus/16)
                price_west+=count_of_16_west*us_west["8xlarge"]
                cpus=cpus-(count_of_16_west*16)
                new_nodes_west.append("8xlarge")
                count_west.append(count_of_16_west)
                countw+=1
            elif(cpus>=8 and cpus<16):
                count_of_8_west=int(cpus/8)
                price_west+=count_of_8_west*us_west["4xlarge"]
                cpus=cpus-(count_of_8_west*8)
                new_nodes_west.append("4xlarge")
                count_west.append(count_of_8_west)
                countw+=1
            elif(cpus>=4 and cpus<8):
                count_of_4_west=int(cpus/4)
                price_west+=count_of_4_west*us_west["2xlarge"]
                cpus=cpus-(count_of_4_west*4)
                new_nodes_west.append("2xlarge")
                count_west.append(count_of_4_west)
                countw+=1
            elif(cpus>=1):
                count_of_1_west=int(cpus/1)
                price_west+=count_of_1_west*us_west["large"]
                cpus=cpus-(count_of_1_west*1)
                new_nodes_west.append("large")
                count_west.append(count_of_1_west)
                countw+=1
    price_east*=hours
    price_west*=hours
    print(price_east)
    if(t==1):
        server(new_nodes_east,count_east,counte,new_nodes_west,count_west,countw,price_east,price_west)
    elif(price_east<=price and price_west<=price and t==3):
        
        server(new_nodes_east, count_east, counte, new_nodes_west, count_west, countw, price_east, price_west)
    elif(t==3 and price_east>price and price_west>price):
        new_nodes_east.clear()
        new_nodes_west.clear()
        count_east.clear()
        count_west.clear()
        type_two(hours,price)
         
def type_two(hours,price):
    
    counte=0
    countw=0
    price=price/hours
    print(price)
    cost=price
    for i in us_east:
            
            if(price>=us_east["10xlarge"]):
                count_of_32_east=int(price/us_east["10xlarge"])
                price=round(price-(count_of_32_east*us_east["10xlarge"]),1)
                new_nodes_east.append("10xlarge")
                count_east.append(count_of_32_east)
                counte+=1
                
                
            elif(price>=us_east["8xlarge"] and price<us_east["10xlarge"]):
                count_of_16_east=int(price/us_east["8xlarge"])
                price=round(price-(count_of_16_east*us_east["8xlarge"]),1)
                new_nodes_east.append("8xlarge")
                count_east.append(count_of_16_east)
                counte+=1
                
                
            elif(price>=us_east["4xlarge"] and price<us_east["8xlarge"]):
                count_of_8_east=int(price/us_east["4xlarge"])
                price=round(price-(count_of_8_east*us_east["4xlarge"]),1)
                new_nodes_east.append("4xlarge")
                count_east.append(count_of_8_east)
                counte+=1
                

            elif(price>=us_east["2xlarge"] and price<us_east["4xlarge"]):
                count_of_4_east=int(price/us_east["2xlarge"])
                price=round(price-(count_of_4_east*us_east["2xlarge"]),1)
                new_nodes_east.append("2xlarge")
                count_east.append(count_of_4_east)
                counte+=1
                

            elif(price>=us_east["xlarge"] and price<us_east["2xlarge"]):
                count_of_2_east=int(price/us_east["xlarge"])
                price=round(price-(count_of_2_east*us_east["xlarge"]),1)
                new_nodes_east.append("xlarge")
                count_east.append(count_of_2_east)
                counte+=1
                
                
            elif(price>=us_east["large"]):
                count_of_1_east=int(price/us_east["large"])
                price=round(price-(count_of_1_east*us_east["large"]),1)
                new_nodes_east.append("large")
                count_east.append(count_of_1_east)
                counte+=1
                

    price=cost            
    for j in us_west:
            if(price>=us_west["10xlarge"]):
                count_of_32_west=int(price/us_west["10xlarge"])
                price=round(price-(count_of_32_west*us_west["10xlarge"]),1)
                new_nodes_west.append("10large")
                count_west.append(count_of_32_west)
                countw+=1
                
                
            elif(price>=us_west["8xlarge"] and price<us_west["10xlarge"]):
                count_of_16_west=int(price/us_west["8xlarge"])
                price=round(price-(count_of_16_west*us_west["8xlarge"]),1)
                new_nodes_west.append("8xlarge")
                count_west.append(count_of_16_west)
                countw+=1
                
                
            elif(price>=us_west["4xlarge"] and price<us_west["8xlarge"]):
                count_of_8_west=int(price/us_west["4xlarge"])
                price=round(price-(count_of_8_west*us_west["4xlarge"]),1)
                new_nodes_west.append("4xlarge")
                count_west.append(count_of_8_west)
                countw+=1
                
                
            elif(price>=us_west["2xlarge"] and price<us_west["4xlarge"]):
                count_of_4_west=int(price/us_west["2xlarge"])
                price=round(price-(count_of_4_west*us_west["2xlarge"]),1)
                new_nodes_west.append("2xlarge")
                count_west.append(count_of_4_west)
                countw+=1
                
                
            elif(price>=us_west["large"]):
                count_of_1_west=int(price/us_west["large"])
                price=round(price-(count_of_1_west*us_west["large"]),1)
                new_nodes_west.append("large")
                count_west.append(count_of_1_west)
                countw+=1
                
    
    price_east=cost*hours
    price_west=cost*hours
    server(new_nodes_east,count_east,counte,new_nodes_west,count_west,countw,price_east,price_west)
    

if(types==1):
    cpus=int(input())
    price_east=0
    price_west=0
    price=0
    type_one(cpus,hours,price_east,price_west,price,1)

    
elif(types==2):
    price=round(int(input("$")))
    type_two(hours,price)
    

elif(types==3):
    cpus=int(input())
    price=int(input("$"))
    price_east=0
    price_west=0
    type_one(cpus,hours,price_east,price_west,price,3)
    
    
