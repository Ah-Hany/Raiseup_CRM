const myDB = db.getSiblingDB("raiseup");

const source = myDB.getCollection("users");

source.find({
    created_at: { $type: "date" }
}).forEach(function(doc) {

    const year = doc.created_at.getUTCFullYear();

    const collectionName = "users_" + year;

    const target = myDB.getCollection(collectionName);

    target.replaceOne(
        { _id: doc._id },
        doc,
        { upsert: true }
    );

});

print("Partitioning Completed Successfully!");
