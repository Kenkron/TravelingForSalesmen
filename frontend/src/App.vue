<template>
  <v-app>
    <v-app-bar class="bg-orange">
      <h2>Traveling Salesman's Travel Planner</h2>
    </v-app-bar>
    <v-navigation-drawer
      permanent
      class="bg-brown"
    >
      <v-list
        class="bg-brown-lighten-1"
      >
        <v-list-subheader>Destinations</v-list-subheader>
        <v-list-item
          v-for="(point, p) in points"
          :key="p"
          :value="point"
          @mouseover="hilight_point(point)"
        >
          {{round(point[0])}}, {{round(point[1])}}
          <v-spacer/>
          <template v-slot:append>
            <v-list-item-avatar end>
              <v-btn
                icon="mdi-close-circle-outline"
                @click="remove_point(p)"/>
            </v-list-item-avatar>
          </template>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-card
        class="mx-auto bg-brown"
        style="width:fit-content; margin-top:32px"
      >
        <v-card-header class="bg-orange">
          Click to add a destination
        </v-card-header>
        <v-img
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Map_of_USA_with_state_names.svg/800px-Map_of_USA_with_state_names.svg.png"
          width="800px"
          height="495px"
          class="mx-auto"
          @click="click_map"
        >
          <canvas
            width="800"
            height="495"
            style="width:100%; height:100%"
            ref="overlay"
          >
          </canvas>
        </v-img>
        <v-card-actions>
          <v-btn
           class="bg-green"
           @click="calculate_route"
          >
            Plan Route
          </v-btn>
          <v-btn
            @click="clear"
          >
            Clear
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios'
import config from './config.js'

export default {
  name: 'App',

  data: () => ({
    points: [],
    hilight: null,
    selected: null,
    path: []
  }),
  methods: {
    draw() {
      let overlay = this.$refs["overlay"]
      let context = overlay.getContext('2d')
      context.clearRect(0, 0, overlay.width, overlay.height)
      let scale = overlay.width * 0.01;
      for (let p of this.points) {
        context.fillStyle = "#FF0000"
        context.beginPath()
        context.arc(p[0] * scale, p[1] * scale, 4, 0, 2 * Math.PI)
        context.fill()
      }
      let hilight = this.hilight
      if (this.hilight) {
        context.fillStyle = "#FF0000"
        context.strokeStyle = "#FF0000"
        context.beginPath()
        context.arc(hilight[0] * scale, hilight[1] * scale, 8, 0, 2 * Math.PI)
        context.fill()
      }
      if (this.path.length > 0) {
        context.strokeStyle = "#00FF00"
        context.lineWidth = 2
        context.beginPath()
        for (let p of this.path) {
          let x = p[0] * scale
          let y = p[1] * scale
          context.lineTo(x, y)
        }
        let p = this.path[0]
        let x = p[0] * scale
        let y = p[1] * scale
        context.lineTo(x, y)
        context.stroke()
      }
    },
    click_map(event) {
      let x = 100 * event.offsetX/event.target.width
      let y = 100 * event.offsetY/event.target.width
      this.points.push([x, y])
      this.path = []
      this.draw()
    },
    remove_point(index) {
      this.points.splice(index, 1)
      this.hilight = null
      this.path = []
      this.draw()
    },
    hilight_point(point) {
      this.hilight = point
      this.draw()
    },
    calculate_route() {
      let self = this
      let request_config = {
        method: "POST",
        url: config.api + "/traveling_salesman",
        data: {
          points: self.points
        }
      }
      axios(request_config).then((res) => {
        if (res.data.path) {
          self.path = res.data.path
          self.points = res.data.path
        }
        self.draw()
      })
    },
    clear() {
      this.points = []
      this.path = []
      this.hilight = null
      this.draw()
    },
    round(number) {
      return number.toFixed(2)
    }
  }
}
</script>
