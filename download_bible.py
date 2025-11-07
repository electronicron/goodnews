#!/usr/bin/env python3
"""
Bible Data Setup Helper
Downloads sample Bible data for testing
"""

import json
import os

# Create bible_data directory
os.makedirs('bible_data', exist_ok=True)

print("=" * 60)
print("Bible Data Setup Helper")
print("=" * 60)
print()

# Create a more comprehensive sample Bible for testing
sample_bible = {
    "translation": "NIV",
    "books": [
        {
            "name": "Genesis",
            "chapters": [
                {
                    "chapter": 1,
                    "verses": [
                        {
                            "verse": 1,
                            "text": "In the beginning God created the heavens and the earth."
                        },
                        {
                            "verse": 27,
                            "text": "So God created mankind in his own image, in the image of God he created them; male and female he created them."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Exodus",
            "chapters": [
                {
                    "chapter": 20,
                    "verses": [
                        {
                            "verse": 3,
                            "text": "You shall have no other gods before me."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Psalm",
            "chapters": [
                {
                    "chapter": 23,
                    "verses": [
                        {
                            "verse": 1,
                            "text": "The Lord is my shepherd, I lack nothing."
                        },
                        {
                            "verse": 4,
                            "text": "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me."
                        }
                    ]
                },
                {
                    "chapter": 46,
                    "verses": [
                        {
                            "verse": 1,
                            "text": "God is our refuge and strength, an ever-present help in trouble."
                        }
                    ]
                },
                {
                    "chapter": 119,
                    "verses": [
                        {
                            "verse": 105,
                            "text": "Your word is a lamp for my feet, a light on my path."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Proverbs",
            "chapters": [
                {
                    "chapter": 3,
                    "verses": [
                        {
                            "verse": 5,
                            "text": "Trust in the Lord with all your heart and lean not on your own understanding;"
                        },
                        {
                            "verse": 6,
                            "text": "in all your ways submit to him, and he will make your paths straight."
                        }
                    ]
                },
                {
                    "chapter": 16,
                    "verses": [
                        {
                            "verse": 3,
                            "text": "Commit to the Lord whatever you do, and he will establish your plans."
                        }
                    ]
                },
                {
                    "chapter": 22,
                    "verses": [
                        {
                            "verse": 6,
                            "text": "Start children off on the way they should go, and even when they are old they will not turn from it."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Isaiah",
            "chapters": [
                {
                    "chapter": 40,
                    "verses": [
                        {
                            "verse": 31,
                            "text": "But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint."
                        }
                    ]
                },
                {
                    "chapter": 41,
                    "verses": [
                        {
                            "verse": 10,
                            "text": "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Jeremiah",
            "chapters": [
                {
                    "chapter": 29,
                    "verses": [
                        {
                            "verse": 11,
                            "text": "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Matthew",
            "chapters": [
                {
                    "chapter": 5,
                    "verses": [
                        {
                            "verse": 14,
                            "text": "You are the light of the world. A town built on a hill cannot be hidden."
                        },
                        {
                            "verse": 16,
                            "text": "In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven."
                        }
                    ]
                },
                {
                    "chapter": 6,
                    "verses": [
                        {
                            "verse": 33,
                            "text": "But seek first his kingdom and his righteousness, and all these things will be given to you as well."
                        }
                    ]
                },
                {
                    "chapter": 7,
                    "verses": [
                        {
                            "verse": 7,
                            "text": "Ask and it will be given to you; seek and you will find; knock and the door will be opened to you."
                        }
                    ]
                },
                {
                    "chapter": 11,
                    "verses": [
                        {
                            "verse": 28,
                            "text": "Come to me, all you who are weary and burdened, and I will give you rest."
                        }
                    ]
                }
            ]
        },
        {
            "name": "John",
            "chapters": [
                {
                    "chapter": 3,
                    "verses": [
                        {
                            "verse": 16,
                            "text": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."
                        }
                    ]
                },
                {
                    "chapter": 14,
                    "verses": [
                        {
                            "verse": 6,
                            "text": "Jesus answered, I am the way and the truth and the life. No one comes to the Father except through me."
                        },
                        {
                            "verse": 27,
                            "text": "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Romans",
            "chapters": [
                {
                    "chapter": 8,
                    "verses": [
                        {
                            "verse": 28,
                            "text": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose."
                        }
                    ]
                },
                {
                    "chapter": 12,
                    "verses": [
                        {
                            "verse": 2,
                            "text": "Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God's will is—his good, pleasing and perfect will."
                        }
                    ]
                }
            ]
        },
        {
            "name": "1 Corinthians",
            "chapters": [
                {
                    "chapter": 10,
                    "verses": [
                        {
                            "verse": 13,
                            "text": "No temptation has overtaken you except what is common to mankind. And God is faithful; he will not let you be tempted beyond what you can bear. But when you are tempted, he will also provide a way out so that you can endure it."
                        }
                    ]
                },
                {
                    "chapter": 13,
                    "verses": [
                        {
                            "verse": 4,
                            "text": "Love is patient, love is kind. It does not envy, it does not boast, it is not proud."
                        },
                        {
                            "verse": 13,
                            "text": "And now these three remain: faith, hope and love. But the greatest of these is love."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Philippians",
            "chapters": [
                {
                    "chapter": 4,
                    "verses": [
                        {
                            "verse": 6,
                            "text": "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God."
                        },
                        {
                            "verse": 13,
                            "text": "I can do all this through him who gives me strength."
                        }
                    ]
                }
            ]
        },
        {
            "name": "2 Timothy",
            "chapters": [
                {
                    "chapter": 1,
                    "verses": [
                        {
                            "verse": 7,
                            "text": "For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline."
                        }
                    ]
                }
            ]
        },
        {
            "name": "James",
            "chapters": [
                {
                    "chapter": 1,
                    "verses": [
                        {
                            "verse": 2,
                            "text": "Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds,"
                        },
                        {
                            "verse": 3,
                            "text": "because you know that the testing of your faith produces perseverance."
                        }
                    ]
                }
            ]
        },
        {
            "name": "1 John",
            "chapters": [
                {
                    "chapter": 4,
                    "verses": [
                        {
                            "verse": 8,
                            "text": "Whoever does not love does not know God, because God is love."
                        },
                        {
                            "verse": 19,
                            "text": "We love because he first loved us."
                        }
                    ]
                }
            ]
        }
    ]
}

# Save NIV sample
niv_file = 'bible_data/niv.json'
with open(niv_file, 'w', encoding='utf-8') as f:
    json.dump(sample_bible, f, indent=2)

print(f"✓ Created sample NIV Bible data: {niv_file}")
print(f"  Contains {len(sample_bible['books'])} books with popular verses")
print()

# Also create a KJV sample for testing translation switching
kjv_sample = {
    "translation": "KJV",
    "books": [
        {
            "name": "John",
            "chapters": [
                {
                    "chapter": 3,
                    "verses": [
                        {
                            "verse": 16,
                            "text": "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Psalm",
            "chapters": [
                {
                    "chapter": 23,
                    "verses": [
                        {
                            "verse": 1,
                            "text": "The LORD is my shepherd; I shall not want."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Proverbs",
            "chapters": [
                {
                    "chapter": 3,
                    "verses": [
                        {
                            "verse": 5,
                            "text": "Trust in the LORD with all thine heart; and lean not unto thine own understanding."
                        }
                    ]
                }
            ]
        }
    ]
}

kjv_file = 'bible_data/kjv.json'
with open(kjv_file, 'w', encoding='utf-8') as f:
    json.dump(kjv_sample, f, indent=2)

print(f"✓ Created sample KJV Bible data: {kjv_file}")
print(f"  Contains {len(kjv_sample['books'])} books (for testing translation switching)")
print()

print("=" * 60)
print("Setup Complete!")
print("=" * 60)
print()
print("You can now test the display:")
print("  python3 bible_display.py")
print()
print("To switch translations:")
print("  1. Edit config.json")
print("  2. Change 'translation' to 'KJV' or 'NIV'")
print()
print("Note: These are SAMPLE files with limited verses for testing.")
print("For a complete Bible, see INSTALLATION.md for download instructions.")
print()
print("To add more verses, edit the JSON files in bible_data/")
print("Format: See existing verses for structure")
print()
