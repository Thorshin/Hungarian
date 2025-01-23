from rich.console import Console
from rich.table import Table
import rich.box
import sys

if len(sys.argv) != 2:
    print("Usage: python Algo_Hongrois.py fichier.csv")
    sys.exit(1)

file_path = sys.argv[1]


def read_csv_to_matrix(file_path):
    matrix = [] 
    try:
        with open(file_path, 'r') as file:
            for line in file:  
                row = [int(entry) for entry in line.strip().split(';')]
                matrix.append(row)  
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return matrix



def cout_general(zero_encadre):
    somme = 0
    matrix_originale = read_csv_to_matrix(file_path)
    print("\nLe cout general est : ") 
    for i in range(len(matrix_originale)):
        for j in range(len(matrix_originale[0])):
            if (i,j) in zero_encadre:
                somme += matrix_originale[i][j]
                if i == len(matrix_originale) - 1:
                    print(matrix_originale[i][j], " = ", somme)
                else:
                    print(matrix_originale[i][j] ,"+ ", end="")
                
        

def display_matrix(matrix, zero_encadre=[], zero_barre=[]):
    console = Console()
    table = Table(show_header=False, header_style="bold magenta", box=rich.box.SQUARE)
    
    for i, row in enumerate(matrix):
        table.add_row(*[f"[green]{value}[/green]" if (i,j) in zero_encadre 
                       else f"[red]{value}[/red]" if (i,j) in zero_barre 
                       else f"[white]{value}[/white]" 
                       for j, value in enumerate(row)], end_section=True)

    console.print(table)

def display_matrix_blue(matrix, ligne_marque=[], colonne_marque=[]):
    console = Console()
    table = Table(show_header=False, header_style="bold magenta", box=rich.box.SQUARE)
    
    white_elements = []
    print("\nLes colonnes et lignes en bleu sont barrées :\n")
    for i, row in enumerate(matrix):
        table.add_row(*[f"[blue]{value}[/blue]" if (i not in ligne_marque or j in colonne_marque)
                       else (lambda x: white_elements.append(x) or f"[white]{x}[/white]")(value)
                       for j, value in enumerate(row)], end_section=True)

    console.print(table)
    
    return min(white_elements) if white_elements else None


def nombre_de_zero(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element == 0:
                count += 1
    return count

def lignes_sans_zero_encadre(matrix, zero_encadre):
    return [i for i in range(len(matrix)) if not any(coord[0] == i for coord in zero_encadre)]

def calcul_colonne_marque(ligne_sans_zero_encadre, matrix, zero_barre):
    colonnes_par_ligne = []
    for ligne in ligne_sans_zero_encadre:
        for j in range(len(matrix[0])):
            if (ligne,j) in zero_barre: 
                colonnes_par_ligne.append(j)
    return colonnes_par_ligne

def calcul_ligne_marque(new_colonne, matrix, zero_encadre):
    lignes_marquees = []

    for i in range(len(matrix)):
        for col in new_colonne:
            if (i, col) in zero_encadre:
                if i not in lignes_marquees:
                    lignes_marquees.append(i)
                    
    return lignes_marquees

def update_matrix(matrix, ligne_marque, colonne_marque, minimum):
    new_matrix = [[value for value in row] for row in matrix]  

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in ligne_marque and j not in colonne_marque:
                new_matrix[i][j] -= minimum
            elif i not in ligne_marque and j in colonne_marque:
                new_matrix[i][j] += minimum
            
    return new_matrix


def affectation(matrix):
    zero_encadre = []
    zero_barre = []
    
    while (len(zero_encadre) + len(zero_barre)) != nombre_de_zero(matrix):
        tab = []
        for i, row in enumerate(matrix):
            counter = 0
            for j, element in enumerate(row):
                if element == 0 and (i,j) not in zero_barre and (i,j) not in zero_encadre:
                    counter += 1
            tab.append(counter)
        
        try:
            non_zero_counts = [x for x in tab if x > 0]
            if not non_zero_counts:  
                break
            min_count = min(non_zero_counts)
            index = tab.index(min_count)
            

            index2 = None
            for j, element in enumerate(matrix[index]):
                if element == 0 and (index,j) not in zero_barre and (index,j) not in zero_encadre:
                    index2 = j
                    zero_encadre.append((index,j))
                    break
            
            if index2 is not None:
                for j, element in enumerate(matrix[index]):
                    if element == 0 and j != index2 and (index,j) not in zero_barre:
                        zero_barre.append((index,j))
                
                for i in range(len(matrix)):
                    if matrix[i][index2] == 0 and i != index and (i,index2) not in zero_barre:
                        zero_barre.append((i,index2))
                        
        except ValueError:
            break  
    
    print("\nLes zeros en vert sont les zeros encadres et ceux en rouge sont les zeros barres :\n")
    display_matrix(matrix, zero_encadre, zero_barre)
    if len(zero_encadre) >= len(matrix):
        cout_general(zero_encadre)
        return

    ligne_marque = lignes_sans_zero_encadre(matrix, zero_encadre)
    colonne_marque = []
    new_colonne = []
    new_ligne = []

    while True:
        new_colonne = calcul_colonne_marque(ligne_marque, matrix, zero_barre)
        new_ligne = calcul_ligne_marque(new_colonne, matrix, zero_encadre)
        
        has_new_elements = False
        for col in new_colonne:
            if col not in colonne_marque:
                colonne_marque.append(col)
                has_new_elements = True
        
        for ligne in new_ligne:
            if ligne not in ligne_marque:
                ligne_marque.append(ligne)
                has_new_elements = True

        if not has_new_elements:
            break
            
        minimum = display_matrix_blue(matrix, ligne_marque, colonne_marque)
        matrix = update_matrix(matrix, ligne_marque, colonne_marque, minimum)
        print("\nLa nouvelle matrice :\n")
        display_matrix(matrix)
        affectation(matrix)
     
matrix = read_csv_to_matrix(file_path)
    
for row in matrix:
    min_value = min(row)
    for j in range(len(row)):
        row[j] -= min_value


num_columns = len(matrix[0])
for col in range(num_columns):
    column_values = [matrix[row][col] for row in range(len(matrix))]
    min_value = min(column_values)
    for row in range(len(matrix)):
        matrix[row][col] -= min_value

print("\nOn soustrait dabord le cout minimal dans les rangees et dans les colonnes :\n")
display_matrix(matrix)
affectation(matrix)
