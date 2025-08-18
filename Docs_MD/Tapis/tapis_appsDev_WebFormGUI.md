# Custom Web Form UI

## Add a Web Form UI (Dropdown, Slider, and Text Field)

You can customize the DesignSafe GUI interface by modifying the `"parameters"` section in your `app-definition.json`.

---

### Example JSON Parameters Section

```json
"parameters": [
  {
    "id": "simulation_type",
    "details": {
      "label": "Simulation Type",
      "description": "Choose a type of simulation to run",
      "type": "enumeration"
    },
    "value": {
      "default": "static",
      "enum_values": ["static", "dynamic", "fatigue"]
    }
  },
  {
    "id": "num_iterations",
    "details": {
      "label": "Number of Iterations",
      "description": "How many times to repeat the analysis",
      "type": "number"
    },
    "value": {
      "default": 10
    }
  },
  {
    "id": "notes",
    "details": {
      "label": "Notes",
      "description": "Any notes or comments for this run",
      "type": "string"
    },
    "value": {
      "default": ""
    }
  }
]
```

This gives you:

* A **dropdown** for simulation type
* A **numeric slider or box** for iterations
* A **text field** for notes

---

### Modify `wrapper.sh` to Use Parameters

Update the script to use these values:

```bash
#!/bin/bash
cd $WORK/$JOB_NAME

module load python/3.9

echo "Running simulation type: $simulation_type"
echo "Iterations: $num_iterations"
echo "Notes: $notes"

python run_analysis.py "$input_file" "$simulation_type" "$num_iterations" "$notes"
```

Update your Python code (`run_analysis.py`) to handle extra arguments:

```python
import sys

input_file = sys.argv[1]
simulation_type = sys.argv[2]
num_iterations = int(sys.argv[3])
notes = sys.argv[4]

print(f"Running simulation type: {simulation_type}")
print(f"Notes: {notes}")

for i in range(num_iterations):
    print(f"Iteration {i+1}: Processing {input_file}")
```