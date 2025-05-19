import numpy as np
import matplotlib.pyplot as plt

# Demand distribution as per book (Page 49)
def generate_monthly_demand():
    return np.random.choice([1, 2, 3, 4], p=[1/6, 1/3, 1/3, 1/6])

def inventory_simulation(s, S, initial_inventory, n_months=120, order_lead_time=1,
                         holding_cost_per_unit=1, shortage_cost_per_unit=5):

    current_month = 0
    inventory_on_hand = initial_inventory
    total_ordered = 0
    total_holding_cost = 0
    total_shortage_cost = 0
    monthly_demand = []
    inventory_history = []

    # Dictionary to hold incoming orders: {arrival_month: amount}
    pipeline_orders = {}

    while current_month < n_months:
        # Receive incoming orders
        if current_month in pipeline_orders:
            inventory_on_hand += pipeline_orders[current_month]
            del pipeline_orders[current_month]

        # Generate this month's demand
        demand = generate_monthly_demand()
        monthly_demand.append(demand)

        if demand <= inventory_on_hand:
            inventory_on_hand -= demand
            shortage = 0
        else:
            shortage = demand - inventory_on_hand
            inventory_on_hand = 0

        # Costs
        holding_cost = holding_cost_per_unit * inventory_on_hand
        shortage_cost = shortage_cost_per_unit * shortage
        total_holding_cost += holding_cost
        total_shortage_cost += shortage_cost

        # Decision: place an order?
        if inventory_on_hand < s:
            order_amount = S - inventory_on_hand
            pipeline_orders[current_month + order_lead_time] = order_amount
            total_ordered += order_amount

        inventory_history.append(inventory_on_hand)
        current_month += 1

    avg_monthly_cost = (total_holding_cost + total_shortage_cost) / n_months

    # Output
    print("\n--- Inventory Simulation Summary ---")
    print(f"(s = {s}, S = {S})")
    print(f"Total Ordered Units: {total_ordered}")
    print(f"Total Holding Cost: {total_holding_cost:.2f}")
    print(f"Total Shortage Cost: {total_shortage_cost:.2f}")
    print(f"Average Monthly Cost: {avg_monthly_cost:.2f}")

    # Plot inventory level over months
    plt.figure(figsize=(10,5))
    plt.plot(inventory_history, label="Inventory Level")
    plt.title("Inventory Level Over Time")
    plt.xlabel("Month")
    plt.ylabel("Inventory on Hand")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# === Accept User Inputs ===
try:
    s = int(input("Enter reorder point (s): "))
    S = int(input("Enter order-up-to level (S): "))
    initial_inventory = int(input("Enter initial inventory: "))
    n_months = int(input("Enter number of months to simulate: "))
    holding_cost_per_unit = float(input("Enter holding cost per unit: "))
    shortage_cost_per_unit = float(input("Enter shortage cost per unit: "))

    inventory_simulation(s, S, initial_inventory, n_months,
                         holding_cost_per_unit=holding_cost_per_unit,
                         shortage_cost_per_unit=shortage_cost_per_unit)

except ValueError:
    print("Invalid input! Please enter numeric values.")
