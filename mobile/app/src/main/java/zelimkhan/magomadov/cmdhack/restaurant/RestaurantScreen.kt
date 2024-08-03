package zelimkhan.magomadov.luckycourse.restaurant

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.ramcosta.composedestinations.annotation.Destination
import zelimkhan.magomadov.luckycourse.core.components.category.CATEGORIES_STATES
import zelimkhan.magomadov.luckycourse.core.components.category.Categories
import zelimkhan.magomadov.luckycourse.ui.theme.BackgroundColor
import zelimkhan.magomadov.luckycourse.ui.theme.luckycourseTheme

@Destination
@Composable
fun RestaurantScreen() {
    RestaurantScreenContent()
}

@Composable
fun RestaurantScreenContent() {
    Column(
        modifier = Modifier.fillMaxSize()
    ) {
        Categories(categories = CATEGORIES_STATES)
        LazyColumn(
            contentPadding = PaddingValues(all = 16.dp),
        ) {
            items(10) {
                RestaurantFoodCard(modifier = Modifier.padding(vertical = 8.dp))
            }
        }
    }
}

@Preview
@Composable
private fun Preview() {
    luckycourseTheme {
        Surface(
            modifier = Modifier.fillMaxSize(),
            color = BackgroundColor,
        ) {
            RestaurantScreen()
        }
    }
}