@bot.command()
async def help_(ctx):
    """Display a help message with information on how to use the bot commands."""
    help_message = """
    **Bot Help**:
    1. **/setup_profile** - Set up your profile (age, gender, weight, height, activity level, and goal).
    2. **/nutrition** - Ask for nutritional information about a specific food item.
    3. **/suggest** - Get meal suggestions based on your profile and dietary restrictions.
    4. **/update_profile** - Update your profile information (age, gender, weight, height, etc.).
    5. **/help_** - Displays this help message.
    6. **/preferences** - User preferences based on activity.
    7. **/meal_analysis** - Analyze the user's meal data from the meal tracker.
    8. **/track_meals** - Track meals for the current day.
    After setting up your profile with !setup_profile, you can ask for nutrition or meal suggestions based on your dietary needs.
    Example usage:
        `/nutrition What is the calorie count of an apple?` `/suggest Can you suggest a healthy lunch?`
    """
    await ctx.send(help_message)
