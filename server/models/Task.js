import mongoose from "mongoose";

const TaskSchema = new mongoose.Schema({
  title: String,
  completed: { type: Boolean, default: false },
  timeSpent: { type: Number, default: 0 },
  project: { type: mongoose.Schema.Types.ObjectId, ref: "Project" }
});

export default mongoose.model("Task", TaskSchema);
