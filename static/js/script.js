document.addEventListener("DOMContentLoaded", () => {
  // Smooth scroll for internal links
  const anchorLinks = document.querySelectorAll('a[href^="#"]');

  anchorLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      const targetId = link.getAttribute("href");
      if (!targetId || targetId === "#") return;

      const target = document.querySelector(targetId);
      if (target) {
        event.preventDefault();
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // Quiz
  document.addEventListener("DOMContentLoaded", () => {

  const quizPanel = document.querySelector(".quiz-panel");
  if (!quizPanel) return;
  
  console.log("Quiz script loaded");
  alert("quiz script loaded");

  const quizCard = quizPanel.querySelector(".quiz-card");
  if (!quizCard) return;

  const q = (question, options, answer) => ({
    question,
    options,
    answer,
  });

  const QUIZ_SETS = [
    [
      q("Which vitamin is highest in oranges?", ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"], "Vitamin C"),
      q("Paneer is mainly made from which ingredient?", ["Milk", "Rice", "Potato", "Wheat"], "Milk"),
      q("Dosa batter is usually made with which grain?", ["Rice", "Corn", "Barley", "Oats"], "Rice"),
      q("What is the main ingredient in french fries?", ["Potato", "Paneer", "Bread", "Carrot"], "Potato"),
      q("Chapati is usually made from which flour?", ["Wheat flour", "Rice flour", "Corn flour", "Besan"], "Wheat flour"),
      q("Poha is made from which ingredient?", ["Flattened rice", "Semolina", "Millet", "Sago"], "Flattened rice"),
      q("Which spice gives yellow colour to food?", ["Turmeric", "Cinnamon", "Clove", "Pepper"], "Turmeric"),
      q("Lassi is usually made from which dairy product?", ["Curd", "Milk powder", "Cheese", "Cream"], "Curd"),
      q("Garlic bread is usually topped with which ingredients?", ["Garlic and butter", "Rice and milk", "Sugar and salt", "Potato and curd"], "Garlic and butter"),
      q("Which ingredient is commonly used in kheer?", ["Milk", "Mustard", "Cabbage", "Lemon"], "Milk"),
    ],
    [
      q("Which appliance cooks food using hot air?", ["Air fryer", "Mixer", "Kettle", "Toaster"], "Air fryer"),
      q("Which cooking method uses steam?", ["Steaming", "Frying", "Grilling", "Roasting"], "Steaming"),
      q("Which method uses very little oil?", ["Sautéing", "Deep frying", "Boiling", "Pickling"], "Sautéing"),
      q("What does boiling need?", ["Water", "Butter", "Flour", "Cheese"], "Water"),
      q("Baking is usually done in a/an:", ["Oven", "Tawa", "Pot", "Cup"], "Oven"),
      q("What does chopping mean?", ["Cutting into small pieces", "Boiling slowly", "Mixing quickly", "Serving cold"], "Cutting into small pieces"),
      q("What does grating mean?", ["Making small shreds", "Boiling rice", "Adding salt", "Frying snacks"], "Making small shreds"),
      q("What is marination used for?", ["Adding flavour before cooking", "Cooling food", "Serving food", "Freezing food"], "Adding flavour before cooking"),
      q("What does blending help make?", ["Smoothies", "Chapati", "Toast", "Idli batter only"], "Smoothies"),
      q("What is simmering?", ["Cooking gently on low heat", "Frying on high flame", "Serving hot", "Mixing without heat"], "Cooking gently on low heat"),
    ],
    [
      q("What is the thickening agent in white sauce?", ["Flour", "Salt", "Sugar", "Rice"], "Flour"),
      q("Pasta is usually made from:", ["Wheat flour", "Rice grains", "Potato starch", "Corn leaves"], "Wheat flour"),
      q("Paneer paratha contains which filling?", ["Paneer", "Banana", "Rice", "Apple"], "Paneer"),
      q("Aloo gobi is made using:", ["Potato and cauliflower", "Rice and dal", "Milk and sugar", "Bread and butter"], "Potato and cauliflower"),
      q("Rajma chawal has which main legume?", ["Kidney beans", "Chickpeas", "Lentils", "Peas"], "Kidney beans"),
      q("Chole bhature is made with:", ["Chickpeas", "Corn", "Paneer", "Mango"], "Chickpeas"),
      q("Pav bhaji is usually served with:", ["Pav", "Naan", "Roti", "Rice"], "Pav"),
      q("Khichdi is usually made from:", ["Rice and dal", "Bread and butter", "Flour and milk", "Potato and corn"], "Rice and dal"),
      q("Dal tadka is made using:", ["Lentils", "Milk", "Bread", "Paneer"], "Lentils"),
      q("Masala dosa is often stuffed with:", ["Potato masala", "Sweet cream", "Mango", "Chocolate"], "Potato masala"),
    ],
    [
      q("Jeera means which spice?", ["Cumin", "Cardamom", "Clove", "Saffron"], "Cumin"),
      q("Coriander leaves are also called:", ["Cilantro", "Rosemary", "Bay leaf", "Mint"], "Cilantro"),
      q("Ginger and garlic are commonly used in:", ["Curries", "Ice cream", "Juices only", "Bread only"], "Curries"),
      q("Which spice adds heat to food?", ["Black pepper", "Sugar", "Salt", "Corn"], "Black pepper"),
      q("Which spice is common in sweets?", ["Cardamom", "Mustard", "Cumin", "Fenugreek"], "Cardamom"),
      q("Cinnamon is often used in:", ["Desserts", "Salads only", "Fried rice only", "Soup only"], "Desserts"),
      q("Cloves are known for being:", ["Aromatic spice", "Leafy vegetable", "Dairy item", "Fruit"], "Aromatic spice"),
      q("Mint chutney is made with:", ["Mint", "Paneer", "Rice", "Bread"], "Mint"),
      q("Mustard seeds are often used for:", ["Tempering", "Sweetening", "Baking cake", "Freezing"], "Tempering"),
      q("Curry leaves are common in:", ["South Indian dishes", "Only desserts", "Only juices", "Only salads"], "South Indian dishes"),
    ],
    [
      q("Milkshake is mainly made with:", ["Milk", "Oil", "Salt", "Rice"], "Milk"),
      q("Banana shake needs which fruit?", ["Banana", "Orange", "Apple", "Grapes"], "Banana"),
      q("Mango lassi uses which fruit?", ["Mango", "Lemon", "Pineapple", "Papaya"], "Mango"),
      q("Lemonade is made with:", ["Lemon", "Milk", "Curd", "Rice"], "Lemon"),
      q("Smoothies often include:", ["Fruit and yogurt", "Only salt", "Only flour", "Only bread"], "Fruit and yogurt"),
      q("Coffee is made from:", ["Coffee beans", "Rice grains", "Wheat", "Milk only"], "Coffee beans"),
      q("Tea is made using:", ["Tea leaves", "Corn", "Paneer", "Potato"], "Tea leaves"),
      q("Hot chocolate uses:", ["Cocoa", "Mint", "Mustard", "Rice"], "Cocoa"),
      q("Coconut water is known for being:", ["Refreshing", "Very oily", "Very salty", "Dry"], "Refreshing"),
      q("Fruit salad usually contains:", ["Mixed fruits", "Only rice", "Only bread", "Only spices"], "Mixed fruits"),
    ],
    [
      q("What meal is usually called the first meal of the day?", ["Breakfast", "Dinner", "Snack", "Dessert"], "Breakfast"),
      q("Upma is made using:", ["Semolina", "Rice flour only", "Paneer", "Bread"], "Semolina"),
      q("Uttapam is best described as a:", ["Thick pancake", "Soup", "Juice", "Stuffed sweet"], "Thick pancake"),
      q("Sandwich is usually made with:", ["Bread", "Rice", "Milk", "Dal"], "Bread"),
      q("Samosa is a:", ["Stuffed pastry", "Fruit drink", "Soup bowl", "Sweet cake"], "Stuffed pastry"),
      q("Pakora is usually:", ["Batter-fried snack", "Boiled rice", "Baked fruit", "Milk dessert"], "Batter-fried snack"),
      q("Omelette is made from:", ["Eggs", "Potato", "Paneer", "Curd"], "Eggs"),
      q("Pancake batter commonly uses:", ["Flour and milk", "Rice and dal", "Bread and oil", "Salt and pepper"], "Flour and milk"),
      q("Waffle is cooked in a:", ["Waffle iron", "Pressure cooker", "Tawa", "Kadhai"], "Waffle iron"),
      q("Toast is bread browned by:", ["Heat", "Water", "Steam", "Sugar"], "Heat"),
    ],
    [
      q("Protein helps mainly in:", ["Building muscles", "Making food sweet", "Cooling food", "Changing colour"], "Building muscles"),
      q("Calcium is good for:", ["Bones and teeth", "Hair only", "Eyes only", "Taste only"], "Bones and teeth"),
      q("Iron helps the body with:", ["Blood health", "Sweetness", "Cooling", "Crunchiness"], "Blood health"),
      q("Fiber is helpful for:", ["Digestion", "Frying", "Freezing", "Baking"], "Digestion"),
      q("Vitamin C helps support:", ["Immunity", "Oil absorption only", "Salt level only", "Crunchiness"], "Immunity"),
      q("Carbohydrates are mainly a source of:", ["Energy", "Only taste", "Only colour", "Only water"], "Energy"),
      q("Fats also give:", ["Energy", "Only sweetness", "Only vitamins", "Only fibre"], "Energy"),
      q("Water helps the body stay:", ["Hydrated", "Spicy", "Sweet", "Crunchy"], "Hydrated"),
      q("High sodium food is usually:", ["Very salty", "Very sweet", "Very sour", "Very cold"], "Very salty"),
      q("A balanced meal should have:", ["Carbs, protein and fats", "Only sugar", "Only water", "Only spice"], "Carbs, protein and fats"),
    ],
  ];

  const getDayIndex = () => {
    const now = new Date();
    const localMidnight = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    return Math.floor(localMidnight.getTime() / 86400000) % QUIZ_SETS.length;
  };

  const getBadge = (score) => {
    if (score <= 3) {
      return {
        emoji: "👶",
        title: "Beginner Chef",
        text: "Good start. Keep playing and you will level up fast.",
      };
    }
    if (score <= 6) {
      return {
        emoji: "🍳",
        title: "Home Cook",
        text: "Nice work. Your food knowledge is growing.",
      };
    }
    if (score <= 8) {
      return {
        emoji: "👨‍🍳",
        title: "Master Chef",
        text: "Strong score. You know your food well.",
      };
    }
    return {
      emoji: "🧙",
      title: "Food Wizard",
      text: "Amazing. You are on top of your food game.",
    };
  };

  const dayIndex = getDayIndex();
  const quizSet = QUIZ_SETS[dayIndex];

  let currentIndex = 0;
  let score = 0;
  let answered = false;

  const progressEl = quizPanel.querySelector(".quiz-progress");
  const scoreEl = quizPanel.querySelector(".quiz-score");
  const questionEl = quizPanel.querySelector(".quiz-question");
  const optionsWrap = quizPanel.querySelector(".quiz-options");
  const nextBtn = quizPanel.querySelector(".quiz-next-btn");
  const dayPill = quizPanel.querySelector(".count-pill");

  const renderResult = () => {
    const badge = getBadge(score);

    quizCard.innerHTML = `
      <div class="quiz-result">
        <div class="quiz-result-icon">${badge.emoji}</div>
        <p class="quiz-result-title">Quiz Completed</p>
        <h3>${badge.title}</h3>
        <div class="quiz-result-score">${score}/10</div>
        <p class="quiz-result-text">${badge.text}</p>
        <button type="button" class="quiz-restart-btn">Play Again</button>
      </div>
    `;

    const restartBtn = quizCard.querySelector(".quiz-restart-btn");
    if (restartBtn) {
      restartBtn.addEventListener("click", () => {
        location.reload();
      });
    }
  };

  const renderQuestion = () => {
    const current = quizSet[currentIndex];
    answered = false;

    if (dayPill) dayPill.textContent = `Day ${dayIndex + 1}`;
    if (progressEl) progressEl.textContent = `Question ${currentIndex + 1}/10`;
    if (scoreEl) scoreEl.textContent = `Score: ${score}`;
    if (questionEl) questionEl.textContent = current.question;

    if (optionsWrap) {
      optionsWrap.innerHTML = "";

      current.options.forEach((option) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "quiz-option";
        btn.dataset.answer = option;
        btn.textContent = option;
        optionsWrap.appendChild(btn);
      });
    }

    if (nextBtn) {
      nextBtn.disabled = true;
      nextBtn.textContent = currentIndex === quizSet.length - 1 ? "Finish Quiz →" : "Next Question →";
    }
  };

  if (optionsWrap) {
    optionsWrap.addEventListener("click", (event) => {
      const button = event.target.closest(".quiz-option");
      if (!button || answered) return;

      answered = true;

      const selectedAnswer = button.dataset.answer;
      const current = quizSet[currentIndex];
      const isCorrect = selectedAnswer === current.answer;

      if (isCorrect) score++;

      optionsWrap.querySelectorAll(".quiz-option").forEach((btn) => {
        btn.disabled = true;

        if (btn.dataset.answer === current.answer) {
          btn.classList.add("correct");
        }

        if (btn.dataset.answer === selectedAnswer) {
          btn.classList.add("selected");
          if (!isCorrect) {
            btn.classList.add("wrong");
          }
        }
      });

      if (scoreEl) scoreEl.textContent = `Score: ${score}`;
      if (nextBtn) nextBtn.disabled = false;
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      if (!answered) return;

      if (currentIndex < quizSet.length - 1) {
        currentIndex++;
        renderQuestion();
      } else {
        renderResult();
      }
    });
  }

  renderQuestion();
});


