from database.mongodb import get_database

db = get_database()

collections = [
    "users",
    "qr_codes",
    "qr_scans",
    "customers",
    "orders",
    "products",
    "templates",
    "settings",
    "audit_logs"
]

existing = db.list_collection_names()

for collection in collections:
    if collection not in existing:
        db.create_collection(collection)
        print(f"✅ Created: {collection}")
    else:
        print(f"ℹ️ Already exists: {collection}")

print("\n🎉 Database setup completed!")