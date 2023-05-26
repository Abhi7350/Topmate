const mongoose = require('mongoose');
mongoose.connect('mongodb+srv://ekabhishek7350:XrA3qghtZ5mfnqeJ@cluster0.jbqzlvl.mongodb.net/', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
mongoose.connection.on('connected', () => {
    console.log('Connected to MongoDB');
  });
  const db = mongoose.connection;
  db.once('open', () => {
    console.log('MongoDB connection is ready');
  });
    