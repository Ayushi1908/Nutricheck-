import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("NutriCheck")
root.geometry("600x850")

root.configure(bg="#E8F5E9")


title = tk.Label(
    root,
    text="🌱 NutriCheck",
    font=("Arial", 32, "bold"),
    bg="#E8F5E9",
    fg="#1B5E20"
)

title.pack(pady=(30, 5))


subtitle = tk.Label(
    root,
    text="Make Better Food Choices",
    font=("Arial", 15),
    bg="#E8F5E9",
    fg="#555555"
)

subtitle.pack(pady=(0, 20))



card = tk.Frame(
    root,
    bg="white",
    padx=35,
    pady=25
)

card.pack(
    padx=40,
    fill="both"
)



food_label = tk.Label(
    card,
    text=" Select Your Food",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#1B5E20"
)

food_label.pack(pady=(5, 10))



foods = [
    "Apple",
    "Banana",
    "Roti",
    "Rice",
    "Pizza",
    "Burger",
    "Chips",
    "Soft Drink"
]




nutrition_data = {

    "Apple": {
        "calories": 95,
        "protein": 0.5,
        "carbs": 25,
        "fat": 0.3,
        "advice": "Great choice!  Apples provide fiber and vitamins."
    },

    "Banana": {
        "calories": 105,
        "protein": 1.3,
        "carbs": 27,
        "fat": 0.4,
        "advice": "Good choice!  Bananas provide energy and potassium."
    },

    "Roti": {
        "calories": 100,
        "protein": 3,
        "carbs": 18,
        "fat": 2,
        "advice": "Good choice!  Try pairing roti with vegetables or dal."
    },

    "Rice": {
        "calories": 205,
        "protein": 4.3,
        "carbs": 45,
        "fat": 0.4,
        "advice": "Good energy source!  Add vegetables and a protein source."
    },

    "Pizza": {
        "calories": 285,
        "protein": 12,
        "carbs": 36,
        "fat": 10,
        "advice": "Enjoy occasionally.  Consider vegetables and a smaller portion."
    },

    "Burger": {
        "calories": 295,
        "protein": 17,
        "carbs": 30,
        "fat": 12,
        "advice": "Have occasionally. Consider grilled options and add vegetables."
    },

    "Chips": {
        "calories": 152,
        "protein": 2,
        "carbs": 15,
        "fat": 10,
        "advice": "Best as an occasional snack. 🥔 Try roasted snacks instead."
    },

    "Soft Drink": {
        "calories": 150,
        "protein": 0,
        "carbs": 39,
        "fat": 0,
        "advice": "Try to limit sugary drinks.  Water is a healthier everyday choice."
    }
}




food_choice = tk.StringVar()

food_choice.set("Apple")


food_menu = tk.OptionMenu(
    card,
    food_choice,
    *foods
)

food_menu.config(
    font=("Arial", 13),
    width=15,
    bg="#F1F8E9",
    fg="#1B5E20"
)

food_menu.pack(pady=(0, 20))




quantity_label = tk.Label(
    card,
    text=" Enter Quantity",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#1B5E20"
)

quantity_label.pack(pady=(5, 10))


quantity_entry = tk.Entry(
    card,
    font=("Arial", 15),
    width=15,
    justify="center"
)

quantity_entry.pack(pady=(0, 20))




result_label = tk.Label(
    card,
    text=" Your nutrition result will appear here",
    font=("Arial", 13),
    bg="white",
    fg="#555555",
    justify="left"
)

result_label.pack(pady=15)



def check_food():

    food = food_choice.get()

    try:

        quantity = int(quantity_entry.get())

    except ValueError:

        messagebox.showwarning(
            "Invalid Quantity",
            "Please enter a valid number."
        )

        return


    if quantity <= 0:

        messagebox.showwarning(
            "Invalid Quantity",
            "Quantity must be greater than 0."
        )

        return


    # Calculate nutrition

    calories = nutrition_data[food]["calories"] * quantity

    protein = nutrition_data[food]["protein"] * quantity

    carbs = nutrition_data[food]["carbs"] * quantity

    fat = nutrition_data[food]["fat"] * quantity

    advice = nutrition_data[food]["advice"]


    # Display result

    result_label.config(
        text=
        f" NUTRITION RESULT\n\n"
        f"️ Food: {food}\n"
        f" Quantity: {quantity}\n\n"
        f" Calories: {calories} kcal\n"
        f" Protein: {protein} g\n"
        f" Carbohydrates: {carbs} g\n"
        f" Fat: {fat} g\n\n"
        f" HEALTH TIP\n"
        f"{advice}",
        fg="#333333"
    )




def clear_result():

    quantity_entry.delete(0, tk.END)

    food_choice.set("Apple")

    result_label.config(
        text="📊 Your nutrition result will appear here",
        fg="#555555"
    )




button_frame = tk.Frame(
    card,
    bg="white"
)

button_frame.pack(pady=10)




check_button = tk.Button(
    button_frame,
    text=" CHECK MY FOOD",
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#388E3C",
    activeforeground="white",
    padx=20,
    pady=8,
    command=check_food
)

check_button.pack(side="left", padx=5)




clear_button = tk.Button(
    button_frame,
    text=" CLEAR",
    font=("Arial", 13, "bold"),
    bg="#EEEEEE",
    fg="#333333",
    padx=15,
    pady=8,
    command=clear_result
)

clear_button.pack(side="left", padx=5)




water_count = 0


water_label = tk.Label(
    root,
    text=" DAILY WATER",
    font=("Arial", 18, "bold"),
    bg="#E8F5E9",
    fg="#1B5E20"
)

water_label.pack(pady=(15, 5))


water_count_label = tk.Label(
    root,
    text="Glasses today: 0 / 8",
    font=("Arial", 13),
    bg="#E8F5E9",
    fg="#555555"
)

water_count_label.pack()


def add_water():

    global water_count

    if water_count < 8:

        water_count = water_count + 1

        water_count_label.config(
            text=f"Glasses today: {water_count} / 8"
        )

    if water_count == 8:

        messagebox.showinfo(
            "Water Goal ",
            "Great job! You reached your daily water goal!"
        )


water_button = tk.Button(
    root,
    text=" ADD WATER",
    font=("Arial", 12, "bold"),
    bg="#81C784",
    fg="white",
    padx=20,
    pady=7,
    command=add_water
)

water_button.pack(pady=8)




footer = tk.Label(
    root,
    text=" Eat Smart • Stay Healthy • Live Better",
    font=("Arial", 11),
    bg="#E8F5E9",
    fg="#666666"
)

footer.pack(pady=10)




exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 10),
    command=root.destroy
)

exit_button.pack(pady=5)



root.mainloop()
