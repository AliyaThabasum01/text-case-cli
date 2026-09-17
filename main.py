from converter import convert_text

print("🔤 Text Case CLI")
print("=" * 35)

text = input("Enter text: ").strip()

if not text:
    print("❌ Please enter some text.")
else:
    results = convert_text(text)

    print("\n✨ Results")
    print("=" * 35)

    for name, value in results.items():
        print(f"{name:<12}: {value}")
