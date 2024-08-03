package zelimkhan.magomadov.luckycourse.home

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.ramcosta.composedestinations.annotation.Destination
import com.ramcosta.composedestinations.navigation.DestinationsNavigator
import zelimkhan.magomadov.luckycourse.core.components.category.CATEGORIES_STATES
import zelimkhan.magomadov.luckycourse.core.components.category.Categories
import zelimkhan.magomadov.luckycourse.core.components.category.CategoriesState
import zelimkhan.magomadov.luckycourse.destinations.RestaurantScreenDestination
import zelimkhan.magomadov.luckycourse.ui.theme.BackgroundColor
import zelimkhan.magomadov.luckycourse.ui.theme.luckycourseTheme

@Destination(start = true)
@Composable
fun HomeScreen(
    navigator: DestinationsNavigator
) {
    HomeScreenContent(
        categoriesState = CATEGORIES_STATES,
        restaurants = RESTAURANTS,
        onRestaurantClick = { navigator.navigate(RestaurantScreenDestination()) }
    )
}

@Composable
fun HomeScreenContent(
    categoriesState: List<CategoriesState>,
    restaurants: List<Restaurant>,
    onRestaurantClick: () -> Unit = {},
) {
    Column(modifier = Modifier.fillMaxSize()) {
        Categories(categories = categoriesState)
        RestaurantsList(restaurants = restaurants, onClick = onRestaurantClick)
    }
}

@Composable
fun RestaurantsList(
    restaurants: List<Restaurant>,
    onClick: () -> Unit = {},
) {
    LazyColumn(
        contentPadding = PaddingValues(vertical = 4.dp),
    ) {
        items(restaurants) {
            FoodCard(
                modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                data = it,
                onClick = onClick
            )
        }
    }
}

@Preview
@Composable
private fun Preview() {
    luckycourseTheme {
        Surface(
            modifier = Modifier.fillMaxSize(),
            color = BackgroundColor
        ) {
            HomeScreenContent(
                categoriesState = CATEGORIES_STATES,
                restaurants = RESTAURANTS
            )
        }
    }
}