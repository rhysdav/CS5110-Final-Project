class CourseCatalog:
    '''Contains special classes/technical electives and related skills.
    Required courses are not listed as skills from those courses are automatically added
    to a candidate by default.'''

    COURSES = {
        'cs2612': { 'skills': ['ASP.NET'] },
        'cs3200': { 'skills': ['Javascript', 'React Native', 'React', 'CSS', 'API', 'Cross-platfrom development'] },
        'cs3430': { 'skills': ['Python', 'ML', 'AI'] },
        'cs3450': { 'skills': ['Agile', 'Scrum', 'Application development', 'API', 'UML', 'Architecture design'] },
        'cs3460': { 'skills': ['C++', 'OOP'] },
        'cs4300': { 'skills': ['Teaching', 'Leadership'] },
        'cs4320': { 'skills': ['Data storage', 'Algorithms'] },
        'cs4700': { 'skills': ['Algorithms', 'Grammars', 'PostScript', 'Haskell', 'Prolog'] },
        'cs4720': { 'skills': ['Client/Server', 'Architecture', 'Hardware'] },
        'cs5000': { 'skills': ['Algorithms', 'Grammars'] },
        'cs5050': { 'skills': ['Algorithms'] },
        'cs5060': { 'skills': ['OOD', 'OOA'] },
        'cs5100': { 'skills': ['Windows', 'Desktop Applications', 'GUIs'] },
        'cs5110': { 'skills': ['literally nothing tbh', 'Multi-Agent Systems', 'Game Theory'] },
        'cs5200': { 'skills': ['Distributed Systems', 'OOP', 'Java', 'System Design', 'Architecture Design'] },
        'cs5300': { 'skills': ['Algorithms', 'Architecture'] },
        'cs5400': { 'skills': ['Javascript', 'Data', 'GUIs'] },
        'cs5410': { 'skills': ['Node', 'Game Dev'] },
        'cs5460': { 'skills': ['Computer Secuirty', 'Cyber Security', 'Encription', 'Hashing', 'Authentication'] },
        'cs5550': { 'skills': ['Parallelism', 'Algorithms'] },
        'cs5600': { 'skills': ['ML', 'AI', 'TensorFlow', 'TFLearn', 'Neural Networks', 'Keras', 'Data', 'Lisp'] },
        'cs5650': { 'skills': ['Computer Vision', 'ML', 'AI'] },
        'cs5660': { 'skills': ['Bioinformatics', 'Data'] },
        'cs5700': { 'skills': ['OOP'] },
        'cs5800': { 'skills': ['SQL', 'NoSQL', 'Postgres', 'MySQL', 'DB'] },
    }
