from transformers import BartTokenizer, BartForConditionalGeneration
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def generate_summary(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=350, min_length=200, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

article = "Modern aviation faces significant challenges due to unpredictable and severe weather conditions that threaten both flight safety and operational efficiency. The need for real-time, adaptive routing solutions is paramount to ensure passenger comfort, enhance safety, and optimize fuel consumption. This project, WeatherGuard: SIGMET and Weather Assisted Alternative Routing Tool, introduces a dynamic rerouting system powered by real-time weather data and Significant Meteorological Information (SIGMET). Utilizing a grid-based alternate routing algorithm, WeatherGuard continuously assesses potential flight paths to identify the safest and most fuel-efficient routes, bypassing turbulent and hazardous weather zones. In addition, the system supports emergency scenarios by rapidly recommending the nearest safe landing options based on current weather conditions and aircraft location. Through AeroAPI, OpenWeather, and AviationWeather.gov integrations, the solution achieves a high degree of accuracy in weather avoidance and fuel savings. Experimental results indicate a 70% reduction in turbulence exposure and up to 10% improvement in fuel efficiency. WeatherGuard’s success highlights the potential of AI-driven route optimization in enhancing both safety and sustainability within the aviation industry."
summary = generate_summary(article)
print("Original Text:",article)
print("Summary:",summary)