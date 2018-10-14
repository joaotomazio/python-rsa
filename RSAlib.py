#Grupo Tg014 - Joao Tomazio numero 78039 - Tiago Fernandes numero 77896

def calcula_mdc(e, n):
       '''calcula_mdc : int x int -> int
          calcula_mdc(e, n) devolve maximo divisor comum do par (e, n) utilizando o Algoritmo de Euclides'''
       
       dividendo = n
       divisor = e
       resto = 1
       
       while resto != 0: #Enquanto mdc nao encontrado
              resto = dividendo % divisor
              mdc = divisor
              #Atribuicao para possivel novo ciclo
              dividendo = divisor
              divisor = resto              
       
       return mdc

def calcula_e(n):
       '''calcula_e : int -> int
          calcula_e(n) devolve menor 'e', com 1 < e < n, sendo 'e' e 'n' co-primos'''       
       
       e = 2 #"Candidato a 'e'. Varia ate valor valido para 'e', minimo 2
       
       while calcula_mdc(e, n) != 1: #Enquanto 'e' e 'n' nao forem co-primos
              e = e + 1
       
       return e
              
 
def calcula_d(e, n):
       '''calcula_d : int x int -> int
          calcula_d(e, n) devolve menor 'd' com 'k' inteiro'''
       
       k = 1 #Valor minimo para k
       resto = 1
       
       while resto != 0: #Ciclo acaba quando ((1 + (n * k)) / e) resultar num inteiro
              resto = (1 + (n * k)) % e
              d = (1 + (n * k)) // e
              k = k + 1
              
       return d

def calcula_primo(x):
       '''calcula_primo : int -> int
          calcula_primo(x) devolve x-esimo primo'''
       
       primo_encont = 0 #Numero de primos encontrados
       primo = 1 #Candidato a primo

       while primo_encont < x:
              resto = 1
              divisor = 1
              primo = primo + 1
              
              while resto != 0: #Enquanto divisor nao encontrado para divisao resto 0
                     divisor = divisor + 1
                     resto = primo % divisor
          
                     if divisor == primo: #Se divisor encontrado igual a candidato, este e primo
                            primo_encont = primo_encont + 1
                        
       return primo
       
def encripta(N, i, j):
       '''encripta : int x int x int -> int
          encripta(N, i, j) devolve N encriptado na forma C'''
       
       p = calcula_primo(i)
       q = calcula_primo(j)
       m = p * q
       
       if N >= m: #Erro para N invalido
              raise ValueError("encripta: a mensagem tem de ser inferior a " + str(m))
       else: #Procedimento para encriptar
              n = (p - 1) * (q - 1)
              e = calcula_e(n)
              C = (N ** e) % m
              return C

def decifra(C, i, j):
       '''decifra : int x int x int -> int
          decifra(C, i, j) devolve C decifrado na forma N'''
       
       p = calcula_primo(i)
       q = calcula_primo(j)
       m = p * q
       
       if C >= m: #Erro para C invalido
              raise ValueError("decifra: a mensagem tem de ser inferior a " + str(m))
       else: #Procedimento para decifrar
              n = (p - 1) * (q - 1)
              e = calcula_e(n)
              d = calcula_d(e, n)
              N = (C ** d) % m
              return N