import mongoose from "mongoose";

const ProjectSchema = new mongoose.Schema({
  name: String,
  description: String,
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User" }
});

export default mongoose.model("Project", ProjectSchema);
