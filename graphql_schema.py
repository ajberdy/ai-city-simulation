import sgqlc.types


graphql_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

class Direction(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('NORTH', 'SOUTH', 'EAST', 'WEST')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class RelativeDirection(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('STRAIGHT', 'LEFT', 'RIGHT')


class Scene(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('CARDEMO', 'WELCOME')


String = sgqlc.types.String

class TestStatus(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('PASS', 'FAIL', 'CRASH', 'TIMEOUT', 'INCORRECT')



########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class AuthPayload(sgqlc.types.Type):
    __schema__ = graphql_schema
    token = sgqlc.types.Field(String, graphql_name='token')
    user = sgqlc.types.Field('User', graphql_name='user')


class Car(sgqlc.types.Type):
    __schema__ = graphql_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    location = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='location')


class CarState(sgqlc.types.Type):
    __schema__ = graphql_schema
    last_intersection = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='last_intersection')
    distance_since = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='distance_since')
    direction = sgqlc.types.Field(sgqlc.types.non_null(Direction), graphql_name='direction')


class City(sgqlc.types.Type):
    __schema__ = graphql_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='members')
    state = sgqlc.types.Field(sgqlc.types.non_null('CityState'), graphql_name='state')
    deployment_id = sgqlc.types.Field(String, graphql_name='deploymentId')


class CityState(sgqlc.types.Type):
    __schema__ = graphql_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    city = sgqlc.types.Field(sgqlc.types.non_null(City), graphql_name='city')
    welcome_scene = sgqlc.types.Field(sgqlc.types.non_null('WelcomeScene'), graphql_name='welcomeScene')
    search_tf = sgqlc.types.Field(sgqlc.types.non_null('SearchTf'), graphql_name='searchTf')


class Connection(sgqlc.types.Type):
    __schema__ = graphql_schema
    name = sgqlc.types.Field(String, graphql_name='name')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    start_name = sgqlc.types.Field(String, graphql_name='startName')
    end_name = sgqlc.types.Field(String, graphql_name='endName')
    length = sgqlc.types.Field(Int, graphql_name='length')
    speed = sgqlc.types.Field(Int, graphql_name='speed')
    direction = sgqlc.types.Field(sgqlc.types.non_null(Direction), graphql_name='direction')


class Intersection(sgqlc.types.Type):
    __schema__ = graphql_schema
    name = sgqlc.types.Field(String, graphql_name='name')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='y')
    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='connections')


class Mutation(sgqlc.types.Type):
    __schema__ = graphql_schema
    signup = sgqlc.types.Field(AuthPayload, graphql_name='signup', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('city', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='city', default=None)),
))
    )
    login = sgqlc.types.Field(AuthPayload, graphql_name='login', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    new_city = sgqlc.types.Field(City, graphql_name='newCity', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    update_welcome_string = sgqlc.types.Field('WelcomeScene', graphql_name='updateWelcomeString', args=sgqlc.types.ArgDict((
        ('welcome_string', sgqlc.types.Arg(String, graphql_name='welcomeString', default=None)),
))
    )
    run_tests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TestResult'))), graphql_name='runTests', args=sgqlc.types.ArgDict((
        ('scene', sgqlc.types.Arg(sgqlc.types.non_null(Scene), graphql_name='scene', default=None)),
))
    )
    run_test = sgqlc.types.Field(sgqlc.types.non_null('TestResult'), graphql_name='runTest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('scene', sgqlc.types.Arg(Scene, graphql_name='scene', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('status', sgqlc.types.Arg(TestStatus, graphql_name='status', default=None)),
))
    )
    add_car = sgqlc.types.Field(sgqlc.types.non_null(Car), graphql_name='addCar', args=sgqlc.types.ArgDict((
        ('color', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='color', default=None)),
        ('location', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='location', default=None)),
))
    )
    update_car = sgqlc.types.Field(Car, graphql_name='updateCar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('color', sgqlc.types.Arg(String, graphql_name='color', default=None)),
        ('location', sgqlc.types.Arg(Int, graphql_name='location', default=None)),
))
    )
    select_map = sgqlc.types.Field('SearchRoadGraph', graphql_name='selectMap', args=sgqlc.types.ArgDict((
        ('map_selection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mapSelection', default=None)),
))
    )
    create_map = sgqlc.types.Field('SearchRoadGraph', graphql_name='createMap', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('graph', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='graph', default=None)),
))
    )
    deploy_to_city = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deployToCity', args=sgqlc.types.ArgDict((
        ('commit_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='commitId', default=None)),
        ('tests_passed', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='testsPassed', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = graphql_schema
    city = sgqlc.types.Field(City, graphql_name='city', args=sgqlc.types.ArgDict((
        ('city_id', sgqlc.types.Arg(ID, graphql_name='cityId', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(ID, graphql_name='userId', default=None)),
))
    )
    cities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(City))), graphql_name='cities')
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='users')
    info = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='info')
    welcome_scene = sgqlc.types.Field('WelcomeScene', graphql_name='welcomeScene')
    search_tf = sgqlc.types.Field('SearchTf', graphql_name='searchTf')
    search_road_graph = sgqlc.types.Field('SearchRoadGraph', graphql_name='searchRoadGraph', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )


class SearchAction(sgqlc.types.Type):
    __schema__ = graphql_schema
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    new_car_loc = sgqlc.types.Field(sgqlc.types.non_null('SearchCarLocation'), graphql_name='newCarLoc')


class SearchCarLocation(sgqlc.types.Type):
    __schema__ = graphql_schema
    intersection = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='intersection')
    direction = sgqlc.types.Field(sgqlc.types.non_null(Direction), graphql_name='direction')
    distance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='distance')


class SearchRoadGraph(sgqlc.types.Type):
    __schema__ = graphql_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    intersections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Intersection))), graphql_name='intersections')
    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Connection))), graphql_name='connections')
    start_state = sgqlc.types.Field(CarState, graphql_name='startState')


class SearchState(sgqlc.types.Type):
    __schema__ = graphql_schema
    car_loc = sgqlc.types.Field(sgqlc.types.non_null(SearchCarLocation), graphql_name='carLoc')


class SearchTf(sgqlc.types.Type):
    __schema__ = graphql_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    city_state = sgqlc.types.Field(sgqlc.types.non_null(CityState), graphql_name='cityState')
    start_state = sgqlc.types.Field(sgqlc.types.non_null(SearchState), graphql_name='startState')
    action_buffer = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SearchAction)), graphql_name='actionBuffer')
    road_graph = sgqlc.types.Field(sgqlc.types.non_null(SearchRoadGraph), graphql_name='roadGraph')


class Subscription(sgqlc.types.Type):
    __schema__ = graphql_schema
    new_car = sgqlc.types.Field(Car, graphql_name='newCar')
    new_test_result = sgqlc.types.Field('TestResult', graphql_name='newTestResult')
    update_welcome_scene = sgqlc.types.Field('WelcomeScene', graphql_name='updateWelcomeScene')


class TestResult(sgqlc.types.Type):
    __schema__ = graphql_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    status = sgqlc.types.Field(sgqlc.types.non_null(TestStatus), graphql_name='status')
    tested_by = sgqlc.types.Field('User', graphql_name='testedBy')


class User(sgqlc.types.Type):
    __schema__ = graphql_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    tests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TestResult))), graphql_name='tests')
    city = sgqlc.types.Field(City, graphql_name='city')


class WelcomeScene(sgqlc.types.Type):
    __schema__ = graphql_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    state = sgqlc.types.Field(sgqlc.types.non_null(CityState), graphql_name='state')
    tests = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TestResult)), graphql_name='tests')
    welcome_string = sgqlc.types.Field(String, graphql_name='welcomeString')



########################################################################
# Unions
########################################################################
