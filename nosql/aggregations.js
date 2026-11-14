const crm = db.getSiblingDB("crm");
const raiseup = db.getSiblingDB("raiseup");

// 1. Users per year (all yearly collections)
print("--- 1. Users per year");
raiseup.getCollectionNames()
  .filter(n => /^users_\d{4}$/.test(n))
  .sort()
  .forEach(n => print(n + ": " + raiseup.getCollection(n).countDocuments()));

// 2. Users per governorate in 2020 (case-insensitive)
print("--- 2. Users per governorate (2020)");
printjson(raiseup.users_2020.aggregate([
  { $group: { _id: { $toLower: "$governorate" }, users: { $sum: 1 }, avgAge: { $avg: "$age" } } },
  { $sort: { users: -1 } }
]).toArray());

// 3. Age segments in 2020
print("--- 3. Age segments (2020)");
printjson(raiseup.users_2020.aggregate([
  { $bucket: { groupBy: "$age", boundaries: [0, 18, 25, 35, 45, 60, 120], default: "other", output: { users: { $sum: 1 } } } }
]).toArray());

// 4. Signups per month in 2020
print("--- 4. Signups per month (2020)");
printjson(raiseup.users_2020.aggregate([
  { $group: { _id: { $month: "$created_at" }, signups: { $sum: 1 } } },
  { $sort: { _id: 1 } }
]).toArray());

// 5. Top 5 authors by number of posts
print("--- 5. Top 5 authors");
printjson(crm.posts.aggregate([
  { $group: { _id: "$user_id", posts: { $sum: 1 } } },
  { $sort: { posts: -1 } },
  { $limit: 5 }
]).toArray());
