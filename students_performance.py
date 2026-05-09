from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app = FastAPI(
    title="Intro to FastAPI",
    description="A simple introduction to FastAPI",
    version="1.0.0"
   )

class students(BaseModel):
    name: str
    age: int
    marks: int

    def is_pass(self):            
        if self.marks >= 50:
            return "Pass ✅"
        else:
            return "Fail ❌"

    def get_grade(self):           
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        else:
            return "C"
        
        

@app.post("/students")
def create_student(student: students):
    return {
        "name": student.name,
        "result": student.is_pass(),  
        "grade": student.get_grade()   
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081 ,reload=True)
