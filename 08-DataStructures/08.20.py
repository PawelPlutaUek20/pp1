import json

Computer = {
    "All-in-One": True,
    "Processor Type": "Intel Core i7",
    "Processor Speed": 3.0, #[Ghz]
    "RAM": 8, #[GB]
    "SSD": 1, #[TB]
    "Connections": ["3.5 mm headphone jack",
                    "SDXC card slot",
                    "Four USB 3 ports",
                    "Two Thunderbolt 3 (USB-C) ports",
                    "10/100/1000BASE-T Gigabit Ethernet"
    ],
    "Size and Weight": {
        "Height": 45, #[cm]
        "Width": 52.8, #[cm]
        "Stand depth": 17.5, #[cm]
        "Weight": 5.6 #[kg]
    }
}

with open('komputer.json', 'w') as f:
    json.dump(Computer, f, indent=4)