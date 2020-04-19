class CourseCatalog:
    '''Contains special classes/technical electives and related skills.
    Required courses are not listed as skills from those courses are automatically added
    to a candidate by default.'''

    USU_COURSES = {
        'cs2612': { 'course_number': 'cs2612', 'skills': ['ASP.NET'] },
        'cs3200': { 'course_number': 'cs3200', 'skills': ['JavaScript', 'React Native', 'React', 'CSS', 'API', 'Cross-platfrom development', 'Redux', 'AsyncStorage', 'JSX'] },
        'cs3430': { 'course_number': 'cs3430', 'skills': ['Python', 'ML', 'AI'] },
        'cs3450': { 'course_number': 'cs3450', 'skills': ['Agile', 'Scrum', 'Application development', 'API', 'UML', 'Architecture design'] },
        'cs3460': { 'course_number': 'cs3460', 'skills': ['C++', 'OOP'] },
        'cs4300': { 'course_number': 'cs4300', 'skills': ['Teaching', 'Leadership'] },
        'cs4320': { 'course_number': 'cs4320', 'skills': ['Data storage', 'Algorithms'] },
        'cs4700': { 'course_number': 'cs4700', 'skills': ['Algorithms', 'Grammars', 'PostScript', 'Haskell', 'Prolog'] },
        'cs4720': { 'course_number': 'cs4720', 'skills': ['Client/Server', 'Architecture', 'Hardware'] },
        'cs5000': { 'course_number': 'cs5000', 'skills': ['Algorithms', 'Grammars'] },
        'cs5050': { 'course_number': 'cs5050', 'skills': ['Algorithms'] },
        'cs5060': { 'course_number': 'cs5060', 'skills': ['OOD', 'OOA'] },
        'cs5100': { 'course_number': 'cs5100', 'skills': ['Windows', 'Desktop Applications', 'GUIs'] },
        'cs5110': { 'course_number': 'cs5110', 'skills': ['Multi-Agent Systems', 'Game Theory'] },
        'cs5200': { 'course_number': 'cs5200', 'skills': ['Distributed Systems', 'OOP', 'Java', 'System Design', 'Architecture Design'] },
        'cs5300': { 'course_number': 'cs5300', 'skills': ['Algorithms', 'Architecture'] },
        'cs5400': { 'course_number': 'cs5400', 'skills': ['JavaScript', 'Data', 'GUIs'] },
        'cs5410': { 'course_number': 'cs5410', 'skills': ['Node', 'Game Dev'] },
        'cs5460': { 'course_number': 'cs5460', 'skills': ['Computer Security', 'Cyber Security', 'Encription', 'Hashing', 'Authentication'] },
        'cs5550': { 'course_number': 'cs5550', 'skills': ['Parallelism', 'Algorithms'] },
        'cs5600': { 'course_number': 'cs5600', 'skills': ['ML', 'AI', 'TensorFlow', 'TFLearn', 'Neural Networks', 'Keras', 'Data', 'Lisp'] },
        'cs5650': { 'course_number': 'cs5650', 'skills': ['Computer Vision', 'ML', 'AI'] },
        'cs5660': { 'course_number': 'cs5660', 'skills': ['Bioinformatics', 'Data'] },
        'cs5700': { 'course_number': 'cs5700', 'skills': ['OOP'] },
        'cs5800': { 'course_number': 'cs5800', 'skills': ['SQL', 'NoSQL', 'Postgres', 'MySQL', 'DB'] },
    }

    # From DevPoint
    BOOTCAMP_COURSES = {
        'UofU_WEBDEV' : { 'course_number': 'WEBDEV_FULL', 'skills': ['Ruby', 'OOP', 'Git', 'Ruby on Rails', 'SQL', 'Postgres', 'Bootstrap', 'Authentication', 'JavaScript', 'jQuery', 'ReactJS', 'Heroku', 'CSS', 'HTML'] },
        'UNLV_WEBDEV' : { 'course_number': 'WEBDEV_FULL', 'skills': ['Ruby', 'OOP', 'Git', 'Ruby on Rails', 'SQL', 'Postgres', 'Bootstrap', 'PHP', 'Babel', 'Webpack', 'ReactJS', 'Heroku', 'CSS', 'HTML'] },
    }
