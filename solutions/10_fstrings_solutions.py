import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  SOLUTIONS 10: f-strings and Formatting ✅
"""
print("Exercise 1:")
price = 42.5
print(f"Price: RM{price:.2f}")

print("\nExercise 2:")
population = 32365999
print(f"Population: {population:,}")

print("\nExercise 3:")
items = [
    ("Nasi Lemak", 5.50, 2),
    ("Roti Canai", 2.50, 3),
    ("Teh Tarik", 1.80, 5),
    ("Maggi Goreng", 7.00, 1),
]
print(f"  {'Item':<15} {'Price':>8} {'Qty':>5} {'Total':>9}")
print(f"  {'─' * 40}")
grand_total = 0
for name, price, qty in items:
    total = price * qty
    grand_total += total
    print(f"  {name:<15} RM{price:>5.2f} {qty:>5} RM{total:>6.2f}")
print(f"  {'─' * 40}")
print(f"  {'Grand Total':<15} {'':>8} {'':>5} RM{grand_total:>6.2f}")

print("\nExercise 4:")
pass_rate = 0.8725
print(f"Pass rate: {pass_rate:.1%}")

print("\nExercise 5:")
fruits = ["durian", "rambutan", "mangosteen", "papaya"]
result = ", ".join(fruits[:-1]) + " and " + fruits[-1]
print(result)

print("\nExercise 6:")
items = [("Nasi Lemak", 5.50), ("Teh Tarik", 1.80), ("Roti Canai", 2.50)]
subtotal = sum(p for _, p in items)
tax = subtotal * 0.06
total = subtotal + tax

receipt = f"""
╔══════════════════════════════════╗
║      🍽️  MAMAK CORNER  🍽️        ║
║     Jalan Alor, Kuala Lumpur     ║
╠══════════════════════════════════╣"""
for name, price in items:
    receipt += f"\n║  {name:<20} RM{price:>6.2f}  ║"
receipt += f"""
╠══════════════════════════════════╣
║  {'Subtotal':<20} RM{subtotal:>6.2f}  ║
║  {'Tax (6%)':<20} RM{tax:>6.2f}  ║
╠══════════════════════════════════╣
║  {'TOTAL':<20} RM{total:>6.2f}  ║
╚══════════════════════════════════╝
║       Terima kasih! 🙏           ║
╚══════════════════════════════════╝"""
print(receipt)

print("\n✅ All exercises solved!")
