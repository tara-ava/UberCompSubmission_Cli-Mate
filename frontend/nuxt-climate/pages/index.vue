<template>
<div>
	<b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="240"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
    
    <b-carousel-slide img-src="http://localhost:3000/1.png"></b-carousel-slide>
    <b-carousel-slide img-src="http://localhost:3000/2.png"></b-carousel-slide>
    <b-carousel-slide img-src="http://localhost:3000/1.png"></b-carousel-slide>
    
    </b-carousel>
    <div class="py-5">
		<div class="px-5">
			<h2>Recent News</h2>
		</div>
		<b-container fluid=md>
		  <b-row class="p-5">
			<b-col sm="4">
				<b-img left src="http://localhost:3000/1-article 1.jpg" fluid alt="Responsive image"></b-img>
			</b-col>
			
			<b-col sm="8">
				<h2>Carbon Profile: Indonesia</h2>
				<p>Indonesia was the world’s fourth largest emitter of greenhouse gases in 2015. It is the 16th biggest economy and the largest in southeast Asia. Its emissions stem from deforestation and peatland megafires and, to a lesser extent, the burning of fossil fuels for energy.</p>
			</b-col>
		 </b-row>
		</b-container>
		
		<b-container fluid=md>
		  <b-row class="p-5">
			<b-col sm="4">
				<b-img left src="http://localhost:3000/3-article3.jpg" fluid alt="Responsive image"></b-img>
			</b-col>
			
			<b-col sm="8">
				<h2>Bali fights for its beautiful beaches by rethinking waste, plastic trash</h2>
				<p>From single-use plastic bans to education, Bali is digging deep to preserve its pristine reputation and save its tourism industry. Plastic waste has been piling up on Bali, fueled by a lack of infrastructure—or an official plan—to deal with it. Also contributing to bottle- and bag-strewn beaches are growing tourism, ingrained cultural practices, and a lack of awareness about the lifecycle of plastic from disposal, to sea, to washing up on beaches as trash.</p>
			</b-col>
			</b-row>
		</b-container>
		
		<b-container fluid=md>
		  <b-row class="p-5">
			<b-col sm="4">
				<b-img left src="http://localhost:3000/2-article2.jpg" fluid alt="Responsive image"></b-img>
			</b-col>
			
			<b-col sm="8">
				<h2>Low Plastic Waste Recycling in Indonesia</h2>
				<p>Indonesia is the second largest plastic waste contributor in the world after China. Even so, the management of plastic waste is still low, the company's responsibility for their waste is minimal.</p>
			</b-col>
		 </b-row>
		</b-container>
    </div>
</div>

</template>

<script>
export default {
    //middleware: ['auth']
}
</script>
