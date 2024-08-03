package zelimkhan.magomadov.luckycourse

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.annotation.StringRes
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Home
import androidx.compose.material.icons.rounded.Person
import androidx.compose.material.icons.rounded.ShoppingCart
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.navigation.NavController
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import com.ramcosta.composedestinations.DestinationsNavHost
import com.ramcosta.composedestinations.navigation.navigate
import com.ramcosta.composedestinations.spec.DirectionDestinationSpec
import zelimkhan.magomadov.luckycourse.destinations.CartScreenDestination
import zelimkhan.magomadov.luckycourse.destinations.Destination
import zelimkhan.magomadov.luckycourse.destinations.HomeScreenDestination
import zelimkhan.magomadov.luckycourse.destinations.ProfileScreenDestination
import zelimkhan.magomadov.luckycourse.ui.theme.luckycourseTheme

class MainActivity : ComponentActivity() {
    @OptIn(ExperimentalMaterial3Api::class)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            luckycourseTheme {
                val navController = rememberNavController()
                val currentRoute =
                    navController.currentBackStackEntryAsState().value?.destination?.route

                Scaffold(
                    topBar = {
                        TopAppBar(title = { Text(text = "Restaurant") })
                    },
                    bottomBar = {
                        if (currentRoute in listOf(
                                "home_screen",
                                "cart_screen",
                                "profile_screen"
                            )
                        ) {
                            BottomBar(navController)
                        }
                    }
                ) {
                    DestinationsNavHost(
                        modifier = Modifier.padding(it),
                        navController = navController,
                        navGraph = NavGraphs.root
                    )
                }
            }
        }
    }
}

enum class BottomBarDestination(
    val direction: DirectionDestinationSpec,
    val icon: ImageVector,
    @StringRes val label: Int
) {
    Home(HomeScreenDestination, Icons.Rounded.Home, R.string.home_screen),
    Cart(CartScreenDestination, Icons.Rounded.ShoppingCart, R.string.cart_screen),
    Profile(ProfileScreenDestination, Icons.Rounded.Person, R.string.profile_screen),
}

@Composable
fun BottomBar(
    navController: NavController
) {
    val currentDestination: Destination = navController.appCurrentDestinationAsState().value
        ?: NavGraphs.root.startAppDestination

    NavigationBar {
        BottomBarDestination.entries.forEach { destination ->
            NavigationBarItem(
                selected = currentDestination == destination.direction,
                onClick = {
                    navController.navigate(destination.direction)
                },
                icon = {
                    Icon(
                        imageVector = destination.icon,
                        contentDescription = stringResource(id = destination.label)
                    )
                },
                label = { Text(stringResource(destination.label)) },
            )
        }
    }
}

@Preview
@Composable
private fun Preview() {
    luckycourseTheme {
        Surface(
            modifier = Modifier.fillMaxWidth()
        ) {

        }
    }
}