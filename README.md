# Hungarian Algorithm Implementation in Python  

## Description  
This repository contains an implementation of the **Hungarian Algorithm** for solving the assignment problem, where the goal is to minimize the total cost of assigning tasks to agents. The program reads a cost matrix from a CSV file, reduces it, and determines the optimal assignment while providing a step-by-step visualization of the process.  

## Dependencies  
The following Python libraries are required to run the program:  
- `rich`: For visualizing the matrix in the terminal.  
- Standard Python libraries like `csv` and `exceptions`.  

To install the required dependency, run:  
```bash  
pip install rich  
```  

## Usage  
1. Clone the repository:  
```bash  
git clone https://github.com/your-username/hungarian-algorithm.git  
cd hungarian-algorithm  
```  

2. Prepare your cost matrix in a CSV file (e.g., `tableau.csv`) with values separated by semicolons (`;`). Example:  
```csv  
4;1;3  
2;0;5  
3;2;2  
```  

3. Run the script:  
```bash  
python main.py  
```  

4. The program will:  
   - Read the matrix from the CSV file.  
   - Display the reduced matrix after row and column adjustments.  
   - Show the assignment process with zeros encircled (green) or barred (red).  
   - Calculate and display the total cost of the optimal assignment.  

## File Structure  
```
├── main.py                # Main script implementing the algorithm.  
├── tableau.csv            # Sample input file (cost matrix).  
├── README.md              # Documentation.  
```  

## Example Output  
When provided with the following input matrix:  
```
4;1;3  
2;0;5  
3;2;2  
```  
The program outputs:  
- The reduced matrix.  
- The assignment process with zero markings.  
- The total cost of the optimal assignment.  

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## Contributions  
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.  
