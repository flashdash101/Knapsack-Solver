import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
#importing the necessary packages




def knapsack(n, values, weights, limit):
    # Create a 2D matrix to store the maximum value for each subproblem
    # K[i][w] represents the maximum value that can be obtained by choosing from the first i items 
    # with a total weight less than or equal to w
    K = [[0 for w in range(limit + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(limit + 1):
            if i == 0 or w == 0:
                # If there are no items or the weight limit is 0, the maximum value is 0
                K[i][w] = 0
            elif weights[i - 1] <= w:
                # If the weight of item i is less than or equal to w, compare 
                # the value obtained by including item i in the solution with the value 
                # obtained by not including item i in the solution and take the maximum of these two values
                K[i][w] = max(values[i - 1]
                  + K[i - 1][w - weights[i - 1]],
                               K[i - 1][w])
            else:
                # If the weight of item i is greater than w, item i cannot be included in the solution, 
                # so the value is simply copied from the previous row
                K[i][w] = K[i - 1][w]
 
    # Store the result of Knapsack
    res = K[n][limit]
    
    # Create a list to store the items included in the solution
    solution = [0] * n
    
    w = limit
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the top (K[i-1][w]) or from (values[i-1] + K[i-1][w-wt[i-1]]) 
        # as in Knapsack table. If it comes from the latter one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            solution[i-1] = 1
            
            # Since this weight is included its value is deducted
            res = res - values[i-1]
            w = w - weights[i - 1]
    
    # Return a tuple containing two elements: 
    # The list representing which items are included in the optimal solution, and 
    # The maximum value that can be obtained.
    return solution, K[n][limit]



# Create the main window
root = tk.Tk()
root.geometry('500x270')
root.title("Knapsack Solver")

# Create the sliders for inputting values and weights
y = 20
ValueSliderText1 = tk.Label(root, text="Value 1")
ValueSliderText1.place(x=20, y=40)
value_slider1 = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
value_slider1.place(x=100, y=y)

WeightSliderText1 = tk.Label(root, text="Weight 1")
WeightSliderText1.place(x=300, y=35)
weight_slider1 = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
weight_slider1.place(x=380, y=y)

y += 40
ValueSliderText2 = tk.Label(root, text="Value 2")
ValueSliderText2.place(x=20, y=75)
value_slider2 = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
value_slider2.place(x=100, y=y)

WeightSliderText2 = tk.Label(root, text="Weight 2")
WeightSliderText2.place(x=300, y=75)
weight_slider2 = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
weight_slider2.place(x=380, y=y)

y += 40
ValueSliderText3 = tk.Label(root, text="Value 3")
ValueSliderText3.place(x=20, y=120)
value_slider3 = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
value_slider3.place(x=100, y=y)

WeightSliderText3 = tk.Label(root, text="Weight 3")
WeightSliderText3.place(x=300, y=115)
weight_slider3 = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
weight_slider3.place(x=380, y=y)

y += 40
limit_label = tk.Label(root, text=" Weight Limit")
limit_label.place(x=15,y=160)

limit_slider = tk.Scale(root, from_=0, to=25, orient=tk.HORIZONTAL)
limit_slider.place(x=100,y=y)


#Sliders for inputting values and weights
#Lables to display values and weights text


def solve():
    # Get the current values of sliders and limit
    values = [value_slider1.get(), value_slider2.get(), value_slider3.get()]
    weights = [weight_slider1.get(), weight_slider2.get(), weight_slider3.get()]
    limit = limit_slider.get()
    if limit <= 1:
        messagebox.showwarning('Limit', 'Limit is too low please increase')
    else:
        n = len(values)
        solution, objective = knapsack(n, values, weights, limit)
        
        # Display the results in a messagebox
        messagebox.showinfo("Solution", f"Solution: {solution}\nObjective: {objective}")
    

# Create the "Solve" button
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.place(x= 250, y= 200)


def plot_values_weights():
    # Get the current values and weights from the sliders
    values = [value_slider1.get(), value_slider2.get(), value_slider3.get()]
    weights = [weight_slider1.get(), weight_slider2.get(), weight_slider3.get()]

    # Create a bar chart to visualize values and weights
    x_labels = [f'item {i+1}' for i in range(len(values))]  # Generate labels like 'item 1', 'item 2', ...
    
    plt.bar(range(len(values)), values, color='b', label='Values')
    plt.bar(range(len(weights)), weights, color='r', label='Weights')
    plt.xlabel('Item')
    plt.ylabel('Value/Weight')
    plt.xticks(range(len(values)), x_labels)  # Set x-axis ticks and labels
    plt.legend()
    plt.title('Values and Weights of Items')
    plt.show()

# Add a button to trigger the visualization
plot_button = tk.Button(root, text="Plot Values/Weights", command=plot_values_weights)
plot_button.place(x=20, y=240)

def set_random_values():
    # Define your desired range for values and weights
    min_value = 1
    max_value = 10
    min_weight = 1
    max_weight = 10

    # Set random values to the sliders within the specified range
    value_slider1.set(random.randint(min_value, max_value))
    value_slider2.set(random.randint(min_value, max_value))
    value_slider3.set(random.randint(min_value, max_value))
    weight_slider1.set(random.randint(min_weight, max_weight))
    weight_slider2.set(random.randint(min_weight, max_weight))
    weight_slider3.set(random.randint(min_weight, max_weight))
    limit_slider.set(random.randint(0,25))


# Add a button to trigger the randomization
randomize_button = tk.Button(root, text="Randomize", command=set_random_values)
randomize_button.place(x=150, y=200)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "Help" menu
help_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add a "How to Use" option to the Help menu
def show_help():
    # Display a messagebox with usage instructions in a list format
    instructions = (
        "Usage Instructions:",
        "1. Choose some values and some weights.",
        "2. Press 'Solve' to calculate the knapsack solution.",
        "3. If you want, you can click 'Randomize' to set random values and weights.",
    )
    help_text = "\n".join(instructions)
    
    messagebox.showinfo("Help", help_text)


help_menu.add_command(label="How to Use", command=show_help)



if __name__ == "__main__":
    # If this script is executed directly (not imported), run the GUI
    root.mainloop()

