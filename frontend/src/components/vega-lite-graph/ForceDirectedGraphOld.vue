<template>
  <div class="container" ref="1">
    <!-- <transition name="slide"> -->
    <el-menu default-active="1" class="edit-panel" :collapse="!editMode">
      <el-sub-menu index="1">
        <template #title>
          <el-icon><operation /></el-icon>
          <span>Base Config</span>
        </template>
        <el-form
          label-position="top"
          label-width="100px"
          style="max-width: 460px"
          @submit.prevent
          size="small"
          class="form"
          novalidate
        >
          <el-form-item class="form-item-control">
            <div class="form-btn-control">
              <BaseButton @click="simRestart" class="config-btn btn"
                >Default</BaseButton
              >
              <BaseButton @click="simStop" class="config-btn btn"
                >Stop</BaseButton
              >
            </div>
          </el-form-item>
          <el-form-item label="Alpha" class="form-item-control">
            <el-input
              type="number"
              id="alpha"
              v-model="alpha"
              step="0.01"
              min="0"
              max="1"
              @blur="handleBaseBlur('alpha')"
              class="input-control"
            />
          </el-form-item>
          <el-form-item label="AlphaMin" class="form-item-control">
            <el-input
              type="number"
              id="alphaMin"
              v-model="alphaMin"
              step="0.001"
              min="0"
              max="1"
              @blur="handleBaseBlur('alphaMin')"
              class="input-control"
            />
          </el-form-item>
          <el-form-item label="AlphaDecay" class="form-item-control">
            <el-input
              type="number"
              id="alphaDecay"
              v-model="alphaDecay"
              step="0.001"
              min="0"
              max="1"
              @blur="handleBaseBlur('alphaDecay')"
              class="input-control"
            />
          </el-form-item>
          <el-form-item label="AlphaTarget" class="form-item-control">
            <el-input
              type="number"
              id="alphaTarget"
              v-model="alphaTarget"
              step="0.001"
              min="0"
              max="1"
              @blur="handleBaseBlur('alphaTarget')"
              class="input-control"
            />
          </el-form-item>
          <el-form-item label="VelocityDecay" class="form-item-control">
            <el-input
              type="number"
              id="velocityDecay"
              v-model="velocityDecay"
              step="0.01"
              min="0"
              max="1"
              @blur="handleBaseBlur('velocityDecay')"
              class="input-control"
            />
          </el-form-item>
        </el-form>
      </el-sub-menu>
      <el-sub-menu index="2">
        <template #title>
          <el-icon><setting /></el-icon>
          <span>Force Config</span>
        </template>
        <el-sub-menu index="2-1">
          <template #title>
            <el-icon><Location /></el-icon>
            <span>Center Force</span>
          </template>
          <el-form
            label-position="top"
            label-width="100px"
            style="max-width: 460px"
            @submit.prevent
            size="small"
            class="form"
            novalidate
          >
            <el-form-item>
              <div class="btn-label" style="width: 100%">
                <span>Set</span>
                <el-switch
                  v-model="setCenter"
                  size="default"
                  :disabled="false"
                />
              </div>
            </el-form-item>
            <el-form-item>
              <div class="form-btn-control">
                <BaseButton
                  @click="forceDefaultSet('center')"
                  class="config-btn btn"
                  :disabled="!setCenter"
                  >Default</BaseButton
                >
              </div>
            </el-form-item>
            <el-form-item label="CenterX" class="form-item-control">
              <el-input
                :disabled="!setCenter"
                type="number"
                id="centerX"
                v-model.number="centerX"
                step="1"
                min="0"
                :max="defaultForceConfig.center.X * 2"
                class="input-control"
                @blur="handleCenterBlur('X')"
              />
              <el-slider
                :disabled="!setCenter"
                v-model="centerX"
                :min="0"
                :max="defaultForceConfig.center.X * 2"
              />
            </el-form-item>
            <el-form-item label="CenterY" class="form-item-control">
              <el-input
                :disabled="!setCenter"
                type="number"
                id="centerY"
                v-model.number="centerY"
                step="1"
                min="0"
                :max="defaultForceConfig.center.Y * 2"
                class="input-control"
                @blur="handleCenterBlur('Y')"
              />
              <el-slider
                :disabled="!setCenter"
                v-model="centerY"
                :min="0"
                :max="defaultForceConfig.center.Y * 2"
              />
            </el-form-item>
            <el-form-item label="CenterStrength" class="form-item-control">
              <el-input
                :disabled="!setCenter"
                type="number"
                id="centerStrength"
                v-model.number="centerStrength"
                step="0.1"
                min="-1"
                class="input-control"
                @blur="handleCenterBlur('Strength')"
              />
            </el-form-item>
          </el-form>
        </el-sub-menu>
        <el-sub-menu index="2-2">
          <template #title>
            <el-icon><Location /></el-icon>
            <span> Position Force </span>
          </template>

          <el-collapse style="width: 90%; margin-left: auto">
            <el-collapse-item name="1">
              <template #title>
                <div class="btn-label">
                  <span> ForceX </span>
                  <el-switch v-model="setX" size="default" @click.stop />
                </div>
              </template>
              <el-form
                label-position="top"
                label-width="100px"
                style="max-width: 460px; padding-left: 0"
                @submit.prevent
                size="small"
                class="form"
                novalidate
                :disabled="!setX"
              >
                <el-form-item label="X *" class="form-item-control">
                  <el-tabs v-model="forceXMode" @tab-click="handleTabClick">
                    <el-tab-pane
                      label="Number"
                      name="number"
                      style="margin-bottom: 10px"
                    >
                      <el-input
                        type="number"
                        id="xX"
                        v-model.number="xX"
                        step="1"
                        min="0"
                        class="input-control"
                      />
                      <el-slider
                        v-model="xX"
                        :min="0"
                        :max="defaultForceConfig.x.X * 2"
                      />
                    </el-tab-pane>
                    <el-tab-pane label="Aggregate" name="aggregate">
                    </el-tab-pane>
                  </el-tabs>
                </el-form-item>
                <el-form-item label="Strength *" class="form-item-control">
                  <el-input
                    type="number"
                    id="xStrength"
                    v-model.number="xStrength"
                    step="0.1"
                    min="-1"
                    class="input-control"
                  />
                </el-form-item>
              </el-form>
            </el-collapse-item>
            <el-collapse-item name="2">
              <template #title>
                <div class="btn-label">
                  <span> ForceY </span>
                  <el-switch v-model="setY" size="default" />
                </div>
              </template>
              <el-form
                label-position="top"
                label-width="100px"
                style="max-width: 460px; padding-left: 0"
                @submit.prevent
                size="small"
                class="form"
                novalidate
                :disabled="!setY"
              >
                <el-form-item label="Y *" class="form-item-control">
                  <el-input
                    type="number"
                    id="yY"
                    v-model.number="yY"
                    step="1"
                    min="0"
                    class="input-control"
                  />
                  <el-slider
                    v-model="yY"
                    :min="0"
                    :max="defaultForceConfig.y.Y * 2"
                  />
                </el-form-item>
                <el-form-item label="Strength *" class="form-item-control">
                  <el-input
                    type="number"
                    id="yStrength"
                    v-model.number="yStrength"
                    step="0.1"
                    min="-1"
                    class="input-control"
                  />
                </el-form-item>
              </el-form>
            </el-collapse-item>
            <el-collapse-item name="3">
              <template #title>
                <div class="btn-label">
                  <span> ForceR </span>
                  <el-switch v-model="setRadicial" size="default" />
                </div>
              </template>
              <el-form
                label-position="top"
                label-width="100px"
                style="max-width: 460px; padding-left: 0"
                @submit.prevent
                size="small"
                class="form"
                novalidate
                :disabled="!setRadicial"
              >
                <el-form-item label="X" class="form-item-control">
                  <el-input
                    type="number"
                    id="radialX"
                    v-model.number="radialX"
                    step="1"
                    min="0"
                    class="input-control"
                  />
                  <el-slider
                    v-model="radialX"
                    :min="0"
                    :max="defaultForceConfig.radial.X * 2"
                  />
                </el-form-item>
                <el-form-item label="Y" class="form-item-control">
                  <el-input
                    type="number"
                    id="radialY"
                    v-model.number="radialY"
                    step="1"
                    min="0"
                    class="input-control"
                  />
                  <el-slider
                    v-model="radialY"
                    :min="0"
                    :max="defaultForceConfig.radial.Y * 2"
                  />
                </el-form-item>
                <el-form-item label="R *" class="form-item-control">
                  <el-input
                    type="number"
                    id="radialR"
                    v-model.number="radialR"
                    step="1"
                    min="0"
                    class="input-control"
                  />
                  <el-slider v-model="radialR" :min="0" :max="1000" />
                </el-form-item>
                <el-form-item label="Strength *" class="form-item-control">
                  <el-input
                    type="number"
                    id="radialStrength"
                    v-model.number="radialStrength"
                    step="0.1"
                    min="-1"
                    class="input-control"
                  />
                </el-form-item>
              </el-form>
            </el-collapse-item>
          </el-collapse>
        </el-sub-menu>
        <el-sub-menu index="2-3">
          <template #title>
            <el-icon><IconMenu /></el-icon>
            <span> NBody Force </span>
          </template>
          <el-form
            label-position="top"
            label-width="100px"
            style="max-width: 460px"
            @submit.prevent
            size="small"
            class="form"
            novalidate
          >
            <el-form-item>
              <div class="btn-label" style="width: 100%">
                <span>Set</span>
                <el-switch v-model="setManyBody" size="default" />
              </div>
            </el-form-item>
            <el-form-item label="Strength *" class="form-item-control">
              <el-input
                disabled
                type="number"
                id="manyBodyStrength"
                v-model.number="manyBodyStrength"
                step="1"
                min="-500"
                max="500"
                class="input-control"
              />
              <el-slider
                disabled
                v-model="manyBodyStrength"
                :min="-500"
                :max="500"
              />
            </el-form-item>
            <el-form-item label="Theta" class="form-item-control">
              <el-input
                type="number"
                id="manyBodyTheta"
                v-model.number="manyBodyTheta"
                step="0.1"
                min="0"
                class="input-control"
              />
            </el-form-item>
            <el-form-item label="DistanceMin" class="form-item-control">
              <el-input
                :disabled="!setManyBody"
                type="number"
                id="distanceMin"
                v-model.number="manyBodyDistanceMin"
                step="0.1"
                min="0"
                max="1000"
                class="input-control"
              />
              <el-slider
                :disabled="!setManyBody"
                v-model="manyBodyDistanceMin"
                :step="0.1"
                :min="0"
                :max="1000"
              />
            </el-form-item>
            <el-form-item label="DistanceMax" class="form-item-control">
              <el-input
                :disabled="!setManyBody"
                type="number"
                id="manyBodyDistanceMax"
                v-model.number="manyBodyDistanceMax"
                step="0.1"
                min="0"
                max="5000"
                class="input-control"
              />
              <el-slider
                :disabled="!setManyBody"
                v-model="manyBodyDistanceMax"
                :step="0.1"
                :min="0"
                :max="5000"
              />
            </el-form-item>
          </el-form>
        </el-sub-menu>
        <el-sub-menu index="2-4">
          <template #title>
            <el-icon><Warning /></el-icon>
            <span> Collide Force </span>
          </template>
          <el-form
            label-position="top"
            label-width="100px"
            style="max-width: 460px"
            @submit.prevent
            size="small"
            class="form"
            novalidate
          >
            <el-form-item>
              <div class="btn-label" style="width: 100%">
                <span>Set</span>
                <el-switch v-model="setCollide" size="default" />
              </div>
            </el-form-item>
            <el-form-item label="Radius *"> </el-form-item>
            <el-form-item label="Strength" class="form-item-control">
              <el-input
                :disabled="!setCollide"
                type="number"
                id="collideStrength"
                v-model.number="collideStrength"
                step="0.1"
                min="0"
                max="1"
                class="input-control"
              />
            </el-form-item>
            <el-form-item label="Iterations" class="form-item-control">
              <el-input
                :disabled="!setCollide"
                type="number"
                id="collideIterations"
                v-model.number="collideIterations"
                step="1"
                min="0"
                max="500"
                class="input-control"
              />
              <el-slider
                :disabled="!setCollide"
                v-model="collideIterations"
                :min="0"
                :max="500"
              />
            </el-form-item>
          </el-form>
        </el-sub-menu>
        <el-sub-menu index="2-5">
          <template #title>
            <el-icon><Share /></el-icon>
            <span> Link Force </span>
          </template>
          <el-form
            label-position="top"
            label-width="100px"
            style="max-width: 460px"
            @submit.prevent
            size="small"
            class="form"
            novalidate
          >
            <el-form-item>
              <div class="btn-label" style="width: 100%">
                <span>Set</span>
                <el-switch v-model="setLink" size="default" />
              </div>
            </el-form-item>
            <el-form-item label="Distance *" class="form-item-control">
              <el-input
                disabled
                type="number"
                id="linkDistance"
                v-model.number="linkDistance"
                step="1"
                min="0"
                max="300"
                class="input-control"
              />
              <el-slider disabled v-model="linkDistance" :min="0" :max="300" />
            </el-form-item>
            <el-form-item label="Strength *" class="form-item-control">
              <el-input
                :disabled="!setLink"
                type="number"
                id="linkStrength"
                v-model.number="linkStrength"
                step="0.1"
                min="0"
                max="1"
                class="input-control"
              />
            </el-form-item>
            <el-form-item label="Iterations" class="form-item-control">
              <el-input
                :disabled="!setLink"
                type="number"
                id="linkIterations"
                v-model.number="linkIterations"
                step="1"
                min="0"
                max="500"
                class="input-control"
              />
              <el-slider
                :disabled="!setLink"
                v-model="linkIterations"
                :min="0"
                :max="500"
              />
            </el-form-item>
          </el-form>
        </el-sub-menu>
      </el-sub-menu>
    </el-menu>

    <BaseButton
      @click="toggleEditMode"
      class="edit-btn btn"
      :class="{ 'active-btn': editMode }"
    >
      <el-icon size="large" class="icon">
        <Tools />
      </el-icon>
    </BaseButton>
    <BaseCard :inset="true" class="ticks-card"> {{ ticks }} </BaseCard>
    <div id="svg-container"></div>
    <defs style="display: none">
      <svg
        viewBox="0 0 1024 1024"
        xmlns="http://www.w3.org/2000/svg"
        id="defs-remove"
        :width="iconSize"
        :height="iconSize"
      >
        <path
          d="M512 64q190.016 4.992 316.512 131.488T960 512q-4.992 190.016-131.488 316.512T512 960q-190.016-4.992-316.512-131.488T64 512q4.992-190.016 131.488-316.512T512 64zM288 512q0 16 11.008 27.008t27.008 11.008h372q16 0 27.008-11.008t11.008-27.008-11.008-27.008-27.008-11.008H326.016q-16 0-27.008 11.008T288 512z"
        ></path>
      </svg>
      <svg
        id="defs-pin"
        viewBox="0 0 1025 1024"
        xmlns="http://www.w3.org/2000/svg"
        :width="iconSize"
        :height="iconSize"
      >
        <path
          d="M320 839.68l-238.592 174.08c-8.704 6.656-19.456 9.728-29.696 9.728-12.8 0-26.112-5.12-35.84-14.848-17.92-17.92-20.48-46.08-5.12-66.56l212.992-288.256L56.32 487.424C39.936 471.04 36.864 445.44 48.128 425.472c8.192-12.8 76.8-112.64 229.376-75.264 2.56 0.512 5.12 0.512 8.192 1.024 6.144 0.512 13.312 1.024 20.992 2.56 32.256 5.12 89.6-20.48 139.264-62.976 47.616-40.448 78.336-87.552 78.336-120.32 0-7.68 0-15.872-0.512-23.552-1.024-30.72-3.072-77.824 31.744-112.64 41.472-41.472 107.52-45.056 153.088-7.68 1.024 0.512 1.536 1.536 2.56 2.56 24.576 24.064 276.48 275.968 279.04 278.528 21.504 21.504 33.792 50.688 33.792 81.408s-11.776 59.392-33.792 80.896c-34.816 34.816-82.432 33.28-113.664 31.744-7.168 0-15.36-0.512-23.04-0.512-30.72 0-67.584 21.504-103.936 60.928-50.688 55.296-81.92 126.464-79.36 158.72 1.024 10.24 3.072 28.16 3.584 30.72 36.864 149.504-62.976 217.6-74.752 225.28-20.48 12.288-46.592 9.216-62.976-7.168l-165.376-165.376-50.688 35.328z"
        ></path>
      </svg>
      <svg id="defs-dominance" xmlns="http://www.w3.org/2000/svg">
        <image
          href="/pic/dominance.png"
          :width="insightIconSize"
          :height="insightIconSize"
        ></image>
      </svg>
      <svg id="defs-outlier" xmlns="http://www.w3.org/2000/svg">
        <image
          href="/pic/outlier.png"
          :width="insightIconSize"
          :height="insightIconSize"
        ></image>
      </svg>
      <svg id="defs-top2" xmlns="http://www.w3.org/2000/svg">
        <image
          href="/pic/top2.png"
          :width="insightIconSize"
          :height="insightIconSize"
        ></image>
      </svg>
      <svg id="defs-evenness" xmlns="http://www.w3.org/2000/svg">
        <image
          href="/pic/evenness.png"
          :width="insightIconSize"
          :height="insightIconSize"
        ></image>
      </svg>
      <svg id="defs-trend" xmlns="http://www.w3.org/2000/svg">
        <image
          href="/pic/trend.png"
          :width="insightIconSize"
          :height="insightIconSize"
        ></image>
      </svg>
      <svg id="defs-skewness" xmlns="http://www.w3.org/2000/svg">
        <image
          href="/pic/skewness.png"
          :width="insightIconSize"
          :height="insightIconSize"
        ></image>
      </svg>
      <svg id="defs-kurtosis" xmlns="http://www.w3.org/2000/svg">
        <image
          href="/pic/kurtosis.png"
          :width="insightIconSize"
          :height="insightIconSize"
        ></image>
      </svg>
    </defs>
  </div>
</template>

<script>
import {
  Tools,
  Share,
  Menu as IconMenu,
  Location,
  Setting,
  Operation,
  Warning,
  RemoveFilled,
} from "@element-plus/icons-vue";

export default {
  components: {
    Tools,
    Location,
    IconMenu,
    Setting,
    Share,
    Operation,
    Warning,
    Remove: RemoveFilled,
  },
  data() {
    return {
      // color
      defaultLinkColor: "#999",
      defaultNodeColor: "#868e96",
      circleHoveredColor: "#e6fcf5",

      // graph set
      width: null,
      height: null,
      leftCornerCoord: null,
      rightCornerCoord: null,

      circleR: 12,
      circleFocusR: 24,
      // rectWH: 125 * 0.7 + 20,
      rectWidthOffset: 3,
      rectHeightOffset: 13,
      rectHeightBottomOffset: 3,
      rectR: 10,
      vegaLiteR: 125,
      vegaLiteHeight: 100,
      vegaLiteWidth: 100,

      circleLink: 50,
      circleNeighborLink: 100,
      vegaLiteLink: 150,
      vegaLiteLongLink: 300,

      circleStrength: -100,
      circleNeighborStrength: -300,
      vegaLiteStrength: -5000,

      insightNum: 7,
      insightIconSize: 20,
      iconSize: 15,
      iconOffset: 5,

      // show conifg of vega-lite graph
      // (index,view)
      showIndex: new Map(),
      // (index, g)
      pinnedIndex: new Map(),
      // neighbor info
      // (id, [...idn])
      neighborMap: new Map(),
      selectedNode: null,

      simulation: null,
      ticks: 0,
      editMode: false,

      // element plus
      forceXMode: "number",

      /* -------------------------------------------------------------------------- */
      // Base Config
      alpha: 1,
      alphaMin: 0.001,
      alphaDecay: 1 - Math.pow(0.001, 1 / 300),
      alphaTarget: 0,
      velocityDecay: 0.4,
      defaultBaseConfig: {
        alpha: 1,
        alphaMin: 0.001,
        alphaDecay: 1 - Math.pow(0.001, 1 / 300),
        alphaTarget: 0,
        velocityDecay: 0.4,
      },

      // Force Config
      // center config
      setCenter: true,
      centerX: null,
      centerY: null,
      centerStrength: 1,
      // position config
      setX: false,
      xX: null,
      xStrength: 0.1,

      setY: false,
      yY: null,
      yStrength: 0.1,

      setRadicial: false,
      radialX: null,
      radialY: null,
      radialR: 100,
      radialStrength: 0.1,
      // nbody config
      setManyBody: true,
      manyBodyStrength: null,
      manyBodyTheta: 0.9,
      manyBodyDistanceMin: 1,
      manyBodyDistanceMax: 5000,

      // link config
      setLink: true,
      linkDistance: null,
      linkStrength: null,
      linkIterations: 1,

      // collide config
      setCollide: true,
      collideRadius: null,
      collideStrength: 1,
      collideIterations: 1,

      defaultForceConfig: {
        center: {
          X: null,
          Y: null,
          Strength: 1,
        },
        x: {
          X: null,
          Strength: 0.1,
        },
        y: {
          Y: null,
          Strength: 0.1,
        },
        radial: {
          X: null,
          Y: null,
          R: 100,
          Strength: 1,
        },
        manyBody: {
          Strength: null,
          Theta: 0.9,
          DistanceMin: 1,
          DistanceMax: 5000,
        },
        link: {
          Distance: null,
          Strength: null,
          Iterations: 1,
        },
        collide: {
          Radius: null,
          Strength: 1,
          Iterations: 1,
        },
      },
    };
  },
  computed: {
    drawData() {
      return this.$store.getters["force/drawData"];
    },
    vegaLiteData() {
      return this.$store.getters["force/vegaLiteData"];
    },
    carsData() {
      return this.$store.getters["force/carsData"];
    },
  },
  watch: {
    drawData(newVal) {
      if (newVal) {
        //construct the neighbor info
        this.getNeighbourInfo(newVal);
        // draw force graph
        this.drawGraph();
      }
    },

    selectedNode(newVal, oldVal) {
      if (newVal !== oldVal) {
        // get id array of neighbour
        const neighborSet = this.neighborMap.get(newVal);
        const oldNeighborSet = this.neighborMap.get(oldVal);

        this.neighborHighligt(oldVal, oldNeighborSet, "selected", false);

        //  console.log(linkGroup);

        this.neighborHighligt(newVal, neighborSet, "selected", true);
      }
    },
    /* -------------------------------------------------------------------------- */
    // default config
    /* -------------------------------------------------------------------------- */
    alpha(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal > 1) {
          this.alpha = 1;
        } else if (newVal < 0) {
          this.alpha = 0;
        } else {
          this.baseConfigSet("alpha", newVal);
        }
      }
    },
    alphaMin(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal > 1) {
          this.alphaMin = 1;
        } else if (newVal < 0) {
          this.alphaMin = 0;
        } else {
          this.baseConfigSet("alphaMin", newVal);
        }
      }
    },
    alphaDecay(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal > 1) {
          this.alphaDecay = 1;
        } else if (newVal < 0) {
          this.alphaDecay = 0;
        } else {
          this.baseConfigSet("alphaDecay", newVal);
        }
      }
    },
    alphaTarget(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal > 1) {
          this.alphaTarget = 1;
        } else if (newVal < 0) {
          this.alphaTarget = 0;
        } else {
          this.baseConfigSet("alphaTarget", newVal);
        }
      }
    },
    velocityDecay(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal > 1) {
          this.velocityDecay = 1;
        } else if (newVal < 0) {
          this.velocityDecay = 0;
        } else {
          this.baseConfigSet("velocityDecay", newVal);
        }
      }
    },
    /* -------------------------------------------------------------------------- */
    // center force config
    /* -------------------------------------------------------------------------- */
    setCenter(newVal) {
      if (newVal) {
        this.simulation.force(
          "center",
          d3
            .forceCenter(
              this.defaultForceConfig.center.X,
              this.defaultForceConfig.center.Y
            )
            .strength(this.defaultForceConfig.center.Strength)
        );
      } else {
        // remove center force
        this.simulation.force("center", null);
      }
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
    },

    centerX(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal < 0) {
          this.conterX = 0;
        } else {
          this.forceConfigSet("center", "x", newVal);
        }
      }
    },
    centerY(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal < 0) {
          this.conterY = 0;
        } else {
          this.forceConfigSet("center", "y", newVal);
        }
      }
    },
    centerStrength(newVal, oldVal) {
      if (newVal !== oldVal) {
        if (newVal < -1) {
          this.centerStrength = -1;
        } else {
          this.forceConfigSet("center", "strength", newVal);
        }
      }
    },
    /* -------------------------------------------------------------------------- */
    // position force config
    /* -------------------------------------------------------------------------- */
    setX(newVal) {
      if (newVal) {
        const name = this.forceXMode;
        switch (name) {
          case "number":
            this.simulation.force(
              "x",
              d3.forceX(this.xX).strength(this.xStrength)
            );

            break;
          case "aggregate":
            this.simulation.force(
              "x",
              d3
                .forceX()
                .x((d) => {
                  return (+d.group + 1) * 100;
                })
                .strength(this.xStrength)
            );
            break;
        }
      } else {
        this.simulation.force("x", null);
      }
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
    },

    xX(newVal, oldVal) {
      if (this.setX) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.xX = 0;
          } else {
            this.forceConfigSet("x", "x", newVal);
          }
        }
      }
    },
    xStrength(newVal, oldVal) {
      if (this.setX) {
        if (newVal !== oldVal) {
          if (newVal < -1) {
            this.xStrength = -1;
          } else {
            this.forceConfigSet("x", "strength", newVal);
          }
        }
      }
    },

    setY(newVal) {
      if (newVal) {
        this.simulation.force("y", d3.forceY(this.yY).strength(this.yStrength));
      } else {
        this.simulation.force("y", null);
      }
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
    },

    yY(newVal, oldVal) {
      if (this.setY) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.yY = 0;
          } else {
            this.forceConfigSet("y", "y", newVal);
          }
        }
      }
    },
    yStrength(newVal, oldVal) {
      if (this.setY) {
        if (newVal !== oldVal) {
          if (newVal < -1) {
            this.yStrength = -1;
          } else {
            this.forceConfigSet("y", "strength", newVal);
          }
        }
      }
    },

    setRadicial(newVal) {
      if (newVal) {
        this.simulation.force(
          "radial",
          d3
            .forceRadial(this.radialR, this.radialX, this.radialY)
            .strength(this.radialStrength)
        );
      } else {
        this.simulation.force("radial", null);
      }
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
    },
    radialX(newVal, oldVal) {
      if (this.setRadicial) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.radialX = 0;
          } else {
            this.forceConfigSet("radial", "x", newVal);
          }
        }
      }
    },
    radialY(newVal, oldVal) {
      if (this.setRadicial) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.radialY = 0;
          } else {
            this.forceConfigSet("radial", "y", newVal);
          }
        }
      }
    },
    radialR(newVal, oldVal) {
      if (this.setRadicial) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.radialR = 0;
          } else {
            this.forceConfigSet("radial", "radius", newVal);
          }
        }
      }
    },
    radialStrength(newVal, oldVal) {
      if (this.setRadicial) {
        if (newVal !== oldVal) {
          if (newVal < -1) {
            this.radialStrength = -1;
          } else {
            this.forceConfigSet("radial", "strength", newVal);
          }
        }
      }
    },
    /* -------------------------------------------------------------------------- */
    // nbody force config
    /* -------------------------------------------------------------------------- */
    setManyBody(newVal) {
      const that = this;
      if (newVal) {
        this.simulation.force(
          "charge",
          d3
            .forceManyBody()
            .strength(function (d) {
              if (d.showDetail) {
                return that.vegaLiteStrength;
              } else {
                return that.circleStrength;
              }
            })
            .theta(this.manyBodyTheta)
            .distanceMin(this.manyBodyDistanceMin)
            .distanceMax(this.manyBodyDistanceMax)
        );
      } else {
        this.simulation.force("charge", null);
      }
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
    },
    manyBodyStrength(newVal, oldVal) {
      if (this.setManyBody) {
        if (newVal !== oldVal) {
          if (newVal < -500) {
            this.manyBodyStrength = -500;
          } else if (newVal > 500) {
            this.manyBodyStrength = 500;
          } else {
            this.forceConfigSet("charge", "strength", newVal);
          }
        }
      }
    },
    manyBodyTheta(newVal, oldVal) {
      if (this.setManyBody) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.manyBodyTheta = 0;
          } else if (newVal > 1) {
            this.manyBodyTheta = 1;
          } else {
            this.forceConfigSet("charge", "theta", newVal);
          }
        }
      }
    },
    manyBodyDistanceMin(newVal, oldVal) {
      if (this.setManyBody) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.manyBodyDistanceMin = 0;
          } else if (newVal > 1000) {
            this.manyBodyDistanceMin = 1000;
          } else {
            this.forceConfigSet("charge", "distanceMin", newVal);
          }
        }
      }
    },
    manyBodyDistanceMax(newVal, oldVal) {
      if (this.setManyBody) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.manyBodyDistanceMax = 0;
          } else if (newVal > 5000) {
            this.manyBodyDistanceMax = 5000;
          } else {
            this.forceConfigSet("charge", "distanceMax", newVal);
          }
        }
      }
    },
    /* -------------------------------------------------------------------------- */
    // link force config
    /* -------------------------------------------------------------------------- */
    setLink(newVal) {
      if (newVal) {
        const that = this;
        // get links data
        const links = d3
          .select("#svg-container")
          .select("svg")
          .select("g.link-group")
          .selectAll("line")
          .data();
        this.simulation.force(
          "link",
          d3
            .forceLink(links)
            .id((d) => d.id)
            .distance(function (d) {
              if (that.showIndex.size > 0) {
                const show1 = that.showIndex.has(d.source.index);
                const show2 = that.showIndex.has(d.target.index);
                if (show1 || show2) {
                  if (show1 && show2) {
                    return that.vegaLiteLongLink;
                  } else {
                    return that.vegaLiteLink;
                  }
                }
              }
              return that.circleLink;
            })
            .strength(this.linkStrength)
            .iterations(this.linkIterations)
        );
      } else {
        this.simulation.force("link", null);
      }
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
    },

    linkDistance(newVal, oldVal) {
      if (this.setLink) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.linkDistance = 0;
          } else if (newVal > 300) {
            this.linkDistance = 300;
          } else {
            //   console.log("link");
            this.forceConfigSet("link", "distance", newVal);
          }
        }
      }
    },
    linkStrength(newVal, oldVal) {
      if (this.setLink) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.linkStrength = 0;
          } else if (newVal > 1) {
            this.linkStrength = 1;
          } else {
            //   console.log(newVal);
            this.forceConfigSet("link", "strength", newVal);
          }
        }
      }
    },
    linkIterations(newVal, oldVal) {
      if (this.setLink) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.linkIterations = 0;
          } else if (newVal > 500) {
            this.linkIterations = 500;
          } else {
            this.forceConfigSet("link", "iterations", newVal);
          }
        }
      }
    },
    /* -------------------------------------------------------------------------- */
    // collide force config
    /* -------------------------------------------------------------------------- */
    setCollide(newVal) {
      const that = this;
      if (newVal) {
        this.simulation.force(
          "collide",
          d3
            .forceCollide((d) => {
              if (d.showDetail) {
                return that.vegaLiteR;
              } else {
                return that.circleR;
              }
            })
            .strength(this.collideStrength)
            .iterations(this.collideIterations)
        );
      } else {
        this.simulation.force("collide", null);
      }
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
    },
    collideStrength(newVal, oldVal) {
      if (this.setCollide) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.collideStrength = 0;
          } else if (newVal > 1) {
            this.collideStrength = 1;
          } else {
            //   console.log(newVal);
            this.forceConfigSet("collide", "strength", newVal);
          }
        }
      }
    },
    collideIterations(newVal, oldVal) {
      if (this.setCollide) {
        if (newVal !== oldVal) {
          if (newVal < 0) {
            this.collideIterations = 0;
          } else if (newVal > 500) {
            this.collideIterations = 500;
          } else {
            this.forceConfigSet("collide", "iterations", newVal);
          }
        }
      }
    },
  },
  methods: {
    // 载入nodes和links数据
    loadData() {
      // this.$store.dispatch("force/loadData");
      // this.$store.dispatch("force/loadCarsData");
      this.$store.dispatch("force/loadResultData");
    },

    neighborHighligt(id, neighbor, type, enable) {
      const className = type + "-highlight";
      const nodeGroup = d3
        .select("#svg-container")
        .select(".node-group")
        .selectChildren("g");

      const linkGroup = d3
        .select("#svg-container")
        .select(".link-group")
        .selectChildren("line");
      if (neighbor) {
        nodeGroup
          .filter((d) => neighbor.includes(d.id.replace(".", "")))
          .selectChildren("circle, rect")
          .classed(className, enable);
        linkGroup
          .filter(
            (d) =>
              id === d.source.id.replace(".", "") ||
              id === d.target.id.replace(".", "")
          )
          .classed(className, enable);
      }
      if (type === "selected") {
        nodeGroup
          .filter((d) => d.id.replace(".", "") === id)
          .selectChildren("circle, rect")
          .classed("center-highlight", enable);
      }
    },

    // 构造用于查询邻居的 neighborMap
    getNeighbourInfo(data) {
      const links = data.links;
      links.forEach((link) => {
        const sourceId = link.source.replace(".", "");
        const targetId = link.target.replace(".", "");

        if (this.neighborMap.has(sourceId)) {
          this.neighborMap.get(sourceId).push(targetId);
        } else {
          this.neighborMap.set(sourceId, [targetId]);
        }
        if (this.neighborMap.has(targetId)) {
          this.neighborMap.get(targetId).push(sourceId);
        } else {
          this.neighborMap.set(targetId, [sourceId]);
        }
      });
    },

    /* -------------------------------------------------------------------------- */
    // base config
    /* -------------------------------------------------------------------------- */
    // 修正输入为空的情况
    handleBaseBlur(configType) {
      //console.log(target);
      if (!this[configType]) {
        this[configType] = this.defaultBaseConfig[configType];
      }
    },
    simStop() {
      this.simulation.stop();
    },

    // reset all base config to default
    simRestart() {
      if (this.simulation) {
        this.alpha = this.defaultBaseConfig.alpha;
        this.alphaMin = this.defaultBaseConfig.alphaMin;
        this.alphaDecay = this.defaultBaseConfig.alphaDecay;
        this.alphaTarget = this.defaultBaseConfig.alphaTarget;
        this.velocityDecay = this.defaultBaseConfig.velocityDecay;
        this.simulation.alpha(this.defaultBaseConfig.alpha);
        this.simulation.alphaMin(this.defaultBaseConfig.alphaMin);
        this.simulation.alphaDecay(this.defaultBaseConfig.alphaDecay);
        this.simulation.alphaTarget(this.defaultBaseConfig.alphaTarget);
        this.simulation.velocityDecay(this.defaultBaseConfig.velocityDecay);
        this.restart();
      }
    },

    // ?
    // rebind data of dom element(nodes and links) and sim system
    restart() {
      this.ticks = 0;
      // 获取原始绘画数据
      const data = this.drawData;

      //const= d3.select('.node-group')

      const preNodes = this.simulation.nodes();
      // 创建原始数据的copy，因为 force simulation 会改变数组数据
      const links = data.links.map((d) => ({ ...d }));
      const nodes = preNodes.map(function (d) {
        delete d.x;
        delete d.y;
        delete d.vx;
        delete d.vy;

        return d;
      });

      // const nodes = data.nodes.map(function (d, index) {
      //   //console.log(preNodes[index].showDetail);
      //   d["showDetail"] = preNodes[index].showDetail;
      //   d["pinned"] = preNodes[index].pinned;
      //   d["view"] = preNodes[index].view;
      //   d["img "] = preNodes[index].img;
      //   d["rect"] = preNodes[index].rect;
      //   return d;
      // });

      //  console.log(this.showIndex);

      if (this.showIndex.size)
        for (const key of this.showIndex.keys()) {
          nodes[key].showDetail = true;
        }

      if (this.pinnedIndex.size)
        for (const [index, g] of this.pinnedIndex) {
          // this.deleteVegaLite(g, index);
          this.drawVegaLite(g, index, "svg");
        }

      // console.log("nodes", JSON.parse(JSON.stringify(nodes)));

      const nodeG = d3
        .select("#svg-container")
        .select("svg")
        .select("g.node-group");
      const linkG = d3
        .select("#svg-container")
        .select("svg")
        .select("g.link-group");
      //console.log("2: ", nodeG);

      // rebind data of dom elements
      nodeG.selectChildren("g").data(nodes).join("g");
      linkG.selectAll("line").data(links).join("line");
      // rebind data of simulation
      this.simulation.nodes(nodes);
      const linkForce = this.simulation.force("link");
      if (linkForce) this.simulation.force("link").links(links);

      // reset alpha to reheat
      this.simulation.restart();
    },
    // 设置 default config
    baseConfigSet(configType, newVal) {
      this.simulation[configType](newVal);
      if (configType !== "alpha") {
        this.simulation.alpha(this.alpha);
      }
      this.restart();
    },

    /* -------------------------------------------------------------------------- */
    // force config
    /* -------------------------------------------------------------------------- */
    forceConfigSet(forceType, configType, newVal) {
      //console.log(configType, newVal, typeof newVal);
      // since have set new force there, no need to reinitialize
      this.simulation.force(forceType)[configType](newVal);
      //console.log(forceType);

      this.simulation.alpha(this.alpha);
      this.simulation.restart();
      //this.restart();
    },
    forceDefaultSet(forceType) {
      switch (forceType) {
        case "center":
          this.centerX = this.defaultForceConfig.center.X;
          this.centerY = this.defaultForceConfig.center.Y;
          this.centerStrength = this.defaultForceConfig.center.Strength;
          break;
      }
      // reheat and restart
      this.simulation.alpha(this.alpha);
      this.simulation.restart();
      //this.restart();
    },

    /* -------------------------------------------------------------------------- */
    // center force config
    /* -------------------------------------------------------------------------- */

    handleCenterBlur(configType) {
      const name = "center" + configType;
      if (!this[name]) this[name] = this.defaultForceConfig.center[configType];
    },

    /* -------------------------------------------------------------------------- */
    // vegaLite relative
    /* -------------------------------------------------------------------------- */
    drawVegaLite(g, index, mode) {
      const that = this;
      const container = g.select(".vega-lite-container");
      const rect = g.selectChild(".rect");
      const removeIcon = g.selectChild(".remove");
      const pinIcon = g.selectChild(".pin");
      const preView = g.datum().view;
      const rectTitle = g.select(".rect-title");
      const rectTitleName = g.selectChild(".title-name");
      const rectTitleDescription = g.selectChild(".title-description");

      if (preView) {
        // reset the view
        const svg = container.selectChild("svg");
        switch (mode) {
          case "img":
            // 创建反应新状态的img
            svg.classed("not-show", true);
            const imgInfo = g.datum().img;
            preView.toCanvas(5).then((canvas) => {
              // Access the canvas element and export as an image
              const image = document.createElementNS(
                "http://www.w3.org/2000/svg",
                "image"
              );
              image.setAttribute("href", canvas.toDataURL("image/png", 1));
              image.setAttribute("width", imgInfo.width);
              image.setAttribute("height", imgInfo.height);
              image.setAttribute("class", "vega-lite-graph");
              container.node().appendChild(image);
            });
            break;
          case "svg":
            container.selectChild("image").remove();
            svg.classed("not-show", false);

            break;
        }
      } else {
        // let yourVlSpec =JSON.parse( g.datum()["vega-lite"]);
        let yourVlSpec = JSON.parse(g.datum()["vega-lite"][0]);

        // add some options
        yourVlSpec["width"] = this.vegaLiteWidth;
        yourVlSpec["height"] = this.vegaLiteHeight;
        yourVlSpec["usermeta"] = { embedOptions: { renderer: "svg" } };

        // initialization
        vegaEmbed(container.node(), yourVlSpec).then((result) => {
          const view = result.view.background("transparent");
          // record the view
          g.datum().view = view;
          that.showIndex.set(index, view);

          const linkForce = that.simulation.force("link");
          if (linkForce) linkForce.initialize(that.simulation.nodes());
          const bodyForce = that.simulation.force("charge");
          if (bodyForce) {
            that.simulation.force("charge", null);
            that.simulation.force("charge", bodyForce);
          }

          const svg = container.select("svg");

          // add animation
          svg
            .attr("class", "vega-lite-graph")
            .attr("fill-opacity", 0)
            .attr("stroke-opacity", 0)
            .transition()
            .duration(175)
            .attr("fill-opacity", 1)
            .attr("stroke-opacity", 1);
          const width = svg.attr("width");
          const height = svg.attr("height");

          // record the img info
          g.datum().img = {
            width: width,
            height: height,
          };

          const titleHeight = that.iconSize + 2 * that.iconOffset;
          const rectWidth = +width + that.rectWidthOffset * 2;
          const rectHeight = +height + that.rectHeightOffset * 2 + titleHeight;

          const translateX = rectWidth / 2;
          const translateY = rectHeight / 2;
          g.datum().rect = {
            r: Math.sqrt(Math.pow(translateX, 2) + Math.pow(translateY, 2)),
          };
          const collideForce = that.simulation.force("collide");
          if (collideForce) collideForce.initialize(that.simulation.nodes());

          // add ainmation
          rect
            .attr("rx", that.rectR)
            .attr("x", 0)
            .attr("y", 0)
            .attr("width", 0)
            .attr("height", 0)
            .transition()
            .duration(150)
            .attr("x", -translateX)
            .attr("y", -translateY)
            .attr("width", rectWidth)
            .attr("height", rectHeight);

          rectTitle
            .attr("rx", that.rectR)
            .attr("x", 0)
            .attr("y", 0)
            .attr("width", 0)
            .attr("height", 0)
            .transition()
            .duration(150)
            .attr("x", -translateX)
            .attr("y", -translateY)
            .attr("width", rectWidth)
            .attr("height", titleHeight);

          rectTitleName
            .text("This is Name")
            .attr("x", -translateX + that.iconOffset)
            .attr("y", -translateY + that.iconSize + that.iconOffset / 2)
            .attr("font-size", that.iconSize - 2);
          rectTitleDescription
            .text("x axis, y axis")
            .attr("font-size", that.iconSize - 2)
            .attr("x", -translateX + that.iconOffset)
            .attr("y", -translateY + 2 * that.iconSize + 2 * that.iconOffset);
          removeIcon.attr(
            "transform",
            `translate(${translateX - that.iconSize - that.iconOffset},${
              -translateY + that.iconOffset
            })`
          );

          pinIcon.attr(
            "transform",
            `translate(${translateX - 2 * that.iconSize - that.iconOffset},${
              -translateY + that.iconOffset
            })`
          );

          switch (mode) {
            case "img":
              //  console.log("img");
              // 创建反应新状态的img
              svg.classed("not-show", true);
              const imgInfo = g.datum().img;
              view.toCanvas(5).then((canvas) => {
                // Access the canvas element and export as an image
                const image = document.createElementNS(
                  "http://www.w3.org/2000/svg",
                  "image"
                );
                image.setAttribute("href", canvas.toDataURL("image/png", 1));
                image.setAttribute("width", imgInfo.width);
                image.setAttribute("height", imgInfo.height);
                image.setAttribute("class", "vega-lite-graph");
                container.node().appendChild(svg.node());
                container.node().appendChild(image);
              });
              break;
            case "svg":
              // 初始就设置为 pinned 状态
              pinIcon.classed("icon-pinned", true);
              that.pinnedIndex.set(index, g);
              g.datum().pinned = true;
              g.classed("pinned", true);
              g.datum().fx = g.datum().x;
              g.datum().fy = g.datum().y;
              container.node().appendChild(svg.node());
              break;
          }

          container.select("div").remove();
          container.select("details").remove();

          container.style(
            "transform",
            `translate(${-width / 2}px,${
              -height / 2 + that.rectHeightOffset + titleHeight / 2
            }px)`
          );
        });
      }
      that.simulation.alpha(that.alpha);
      that.simulation.restart();
    },
    deleteVegaLite(g, index) {
      this.showIndex.get(index).finalize();
      g.selectAll(".vega-lite-graph").remove();
      g.datum().view = null;
      g.datum().img = null;
      this.pinnedIndex.delete(index);
      this.showIndex.delete(index);
    },
    /* -------------------------------------------------------------------------- */
    // other
    /* -------------------------------------------------------------------------- */
    toggleEditMode() {
      this.editMode = !this.editMode;
    },
    handleTabClick(tab, _event) {
      if (this.setX) {
        const name = tab.props.name;
        switch (name) {
          case "number":
            this.simulation.force(
              "x",
              d3.forceX(this.xX).strength(this.xStrength)
            );

            break;
          case "aggregate":
            this.simulation.force(
              "x",
              d3
                .forceX()
                .x((d) => {
                  return (+d.group + 1) * 100;
                })
                .strength(this.xStrength)
            );
            break;
        }
        this.simulation.alpha(this.alpha);
        this.simulation.restart();
      }
    },
    // initial drawing, create DOM elements and sim system
    drawGraph() {
      const that = this;
      // 获取绘画数据
      const data = this.drawData;
      // 创建原始数据的copy，因为 force simulation 会改变数组数据
      const links = data.links.map((d) => ({ ...d }));
      // 加入更多属性，控制vega-lite图的显示
      const nodes = data.nodes.map((d) => ({
        ...d,
        showDetail: false,
        pinned: false,
        view: null,
        img: null,
        rect: null,
      }));
      //  console.log(data.links);
      // 选择svg container
      const svgContainer = d3.select("#svg-container");
      const defs = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "defs"
      );
      svgContainer.node().appendChild(defs);

      // 获取container的宽和高
      const width = parseInt(svgContainer.style("width"), 10);
      const height = parseInt(svgContainer.style("height"), 10);
      this.leftCornerCoord = [0, 0];
      this.rightCornerCoord = [width, height];
      // 先把svg图和nodes+links 元素画出来
      // 随便设置一个种类的颜色映射
      const color = d3.scaleOrdinal(d3.schemeCategory10);

      // 创建svg
      const svg = svgContainer
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewbox", [-width, -height, width, height])
        .attr("style", "max-width: 100%; height: auto;");
      // 画links
      const linkGroup = svg
        .append("g")
        .attr("class", "link-group")
        .attr("stroke", this.defaultLinkColor)
        .attr("stroke-opacity", 0.6)
        .selectAll("line")
        .data(links)
        .join("line")
        .attr("class", "network-line")
        // link的value值映射到粗细
        .attr(
          "stroke-width",
          1
          // (d) => Math.sqrt(d.value)
        );
      //画nodes

      const circleGroup = svg
        .append("g")
        .attr("class", "node-group")
        .selectAll("g")
        .data(nodes)
        .join("g")
        .append("circle")
        .attr("class", "circle")
        .classed("not-show", function () {
          const gData = d3.select(this.parentNode).datum();
          return gData.showDetail;
        })
        .attr("r", that.circleR)
        .attr("stroke", this.defaultNodeColor)
        // node 进行分类颜色映射
        .attr("fill", "#fff")
        .attr("stroke-width", 1)
        .style("transition", "r 0.2s")
        .on("mouseover", function (event) {
          const d = d3.select(this.parentNode).datum();
          if (!d.showDetail) {
            //颜色变，表示被选中
            d3.select(this)
              .attr("fill", that.circleHoveredColor)
              .attr("r", that.circleFocusR)
              .style("cursor", "pointer");

            d3.select(this.parentNode)
              .select(".insight-icon")
              .attr("transform", "scale(2)");
          }
        })
        .on("mouseout", function (event) {
          const d = d3.select(this.parentNode).datum();
          if (!d.showDetail) {
            d3.select(this).attr("r", that.circleR).attr("fill", "#FFF");
          }
          d3.select(this.parentNode)
            .select(".insight-icon")
            .attr("transform", "scale(1)");
        })
        .on("click", function (event, d) {
          // 获取选择circle对应的container - g元素
          const g = d3.select(this.parentNode);
          that.selectedNode = g.datum().id.replace(".", "");

          if (!g.datum().showDetail) {
            g.datum().showDetail = true;

            const circle = d3.select(this);
            const rect = g.selectChild(".rect");
            const insightIcon = g.selectChild(".insight-icon");
            const rectTitle = g.select(".rect-title");
            const rectText = g.selectChildren(".title-text");

            rect.classed("not-show", false);
            rectTitle.classed("not-show", false);
            rectText.classed("not-show", false);
            circle.classed("not-show", true);
            insightIcon.classed("not-show", true);
            const remove = g
              .append("use")
              .attr("href", "#defs-remove")
              .attr("class", "remove vega-lite-icon")
              .attr("cursor", "pointer")
              .on("click", function () {
                g.datum().showDetail = false;
                g.datum().pinned = false;
                g.classed("pinned", false);
                g.datum().fx = null;
                g.datum().fy = null;
                that.selectedNode = null;
                g.selectChildren(".vega-lite-icon").remove();
                that.deleteVegaLite(g, d.index);
                const collideForce = that.simulation.force("collide");
                const bodyForce = that.simulation.force("charge");
                const linkForce = that.simulation.force("link");
                if (collideForce)
                  collideForce.initialize(that.simulation.nodes());
                if (linkForce) linkForce.initialize(that.simulation.nodes());
                if (bodyForce) {
                  that.simulation.force("charge", null);
                  that.simulation.force("charge", bodyForce);
                }
                rect.classed("not-show", true);
                rectTitle.classed("not-show", true);
                rectText.classed("not-show", true);
                circle
                  .classed("not-show", false)
                  .attr("r", that.circleR)
                  .attr("fill", "#FFF");
                insightIcon.classed("not-show", false);

                that.simulation.alpha(that.alpha);
                that.simulation.restart();
              });

            const pin = g
              .append("use")
              .attr("href", "#defs-pin")
              .attr("class", "pin vega-lite-icon")
              .attr("cursor", "pointer")
              .on("click", togglePin);

            that.drawVegaLite(g, d.index, "img");
          }
        });

      const containerGroup = svg.select("g.node-group").selectChildren("g");
      let groupTmp = 0;
      const iconGroup = containerGroup
        .append("use")
        .attr("href", function () {
          const g = d3.select(this.parentNode);
          //const group = g.datum().group % that.insightNum;
          const group = groupTmp % that.insightNum;
          groupTmp += 1;
          let insightType = null;
          switch (group) {
            case 0:
              insightType = "dominance";
              break;
            case 1:
              insightType = "outlier";
              break;
            case 2:
              insightType = "top2";
              break;
            case 3:
              insightType = "evenness";
              break;
            case 4:
              insightType = "trend";
              break;
            case 5:
              insightType = "skewness";
              break;
            case 6:
              insightType = "kurtosis";
              break;
          }
          return "#defs-" + insightType;
        })
        .attr("class", "insight-icon")
        .attr("x", -this.insightIconSize / 2)
        .attr("y", -this.insightIconSize / 2)
        .attr("pointer-events", "none")
        .style("transition", "transform 0.2s");

      const rectGroup = containerGroup
        .append("rect")
        .attr("class", "rect")
        .classed("not-show", function () {
          const gData = d3.select(this.parentNode).datum();
          return !gData.showDetail;
        })
        .attr("fill", "#fff")
        .attr("stroke", "#ccc")
        .attr("stroke-width", 1.5)
        .attr("cursor", "pointer")
        .on("mouseover", function (event) {
          //颜色变，表示被选中
          const rect = d3.select(this);
          const parentNode = d3.select(this.parentNode);
          const id = parentNode.datum().id.replace(".", "");
          const neighbor = that.neighborMap.get(id);
          that.neighborHighligt(id, neighbor, "hover", true);
          rect.classed("center-highlight", true);
          //  console.log(parentNode.select(".rect-title"));
          parentNode.select(".rect-title").classed("center-highlight", true);
        })
        .on("mouseout", function (event) {
          const rect = d3.select(this);
          const parentNode = d3.select(this.parentNode);
          const id = parentNode.datum().id.replace(".", "");
          const neighbor = that.neighborMap.get(id);
          that.neighborHighligt(id, neighbor, "hover", false);

          if (id !== that.selectedNode) {
            rect.classed("center-highlight", false);
            parentNode.select(".rect-title").classed("center-highlight", false);
          }
        })
        .on("click", function () {
          // 获取对应的container - g元素
          const g = d3.select(this.parentNode);
          that.selectedNode = g.datum().id.replace(".", "");
          console.log("trueId", g.datum().id);
          // d3.select(this).classed("center-highlight", true);
        })
        .on("dblclick", togglePin);

      const titleGroup = containerGroup
        .append("rect")
        .attr("class", "rect-title")
        .classed("not-show", function () {
          const gData = d3.select(this.parentNode).datum();

          return !gData.showDetail;
        })
        .attr("fill", "#e9ecef")
        .attr("stroke", "#ccc")
        .attr("stroke-width", 1.5)
        .attr("pointer-events", "none");

      const nameGroup = containerGroup
        .append("text")
        .classed("not-show", function () {
          const gData = d3.select(this.parentNode).datum();
          return !gData.showDetail;
        })
        .attr("class", "title-text title-name")
        .attr("pointer-events", "none")
        .style("user-select", "none")
        .attr("fill", "#555")
        .attr("font-weight", 600);

      const descriptionGroup = containerGroup
        .append("text")
        .classed("not-show", function () {
          const gData = d3.select(this.parentNode).datum();
          return !gData.showDetail;
        })
        .attr("class", "title-text title-description")
        .attr("pointer-events", "none")
        .attr("fill", "#555")
        .style("user-select", "none");

      const vegaLiteContainerGroup = containerGroup
        .append("g")
        .attr("class", "vega-lite-container");

      /* -------------------------------------------------------------------------- */
      const defaultBaseConfig = this.defaultBaseConfig;
      const defaultForceConfig = this.defaultForceConfig;

      // 力导向系统创建
      const simulation = d3
        .forceSimulation(nodes)
        .force(
          "link",
          // 指明对应的是nodes数据的id属性
          d3
            .forceLink(links)
            .id((d) => d.id)
            // .distance(defaultForceConfig.link.Distance)
            .distance(function (d) {
              if (that.showIndex.size > 0) {
                const show1 = that.showIndex.has(d.source.index);
                const show2 = that.showIndex.has(d.target.index);
                if (show1 || show2) {
                  if (show1 && show2) {
                    return that.vegaLiteLongLink;
                  } else {
                    return that.vegaLiteLink;
                  }
                }

                const sourceId = d.source.id.replace(".", "");
                const targetId = d.target.id.replace(".", "");
                // const sourceNeighbor = that.neighborMap.get(sourceId);
                // const targetNeighbor = that.neighborMap.get(targetId);

                for (const index of that.showIndex.keys()) {
                  const id = nodes[index].id.replace(".", "");
                  //console.log(id);
                  const directNeighbor = that.neighborMap.get(id);
                  if (directNeighbor) {
                    for (const neighbor of directNeighbor) {
                      const secondNeighbor = that.neighborMap.get(neighbor);
                      if (
                        (targetId === neighbor &&
                          secondNeighbor.includes(sourceId)) ||
                        (sourceId === neighbor &&
                          secondNeighbor.includes(targetId))
                      ) {
                        return that.circleNeighborLink;
                      }
                    }
                  }
                }
              }
              return that.circleLink;
            })
            .iterations(defaultForceConfig.link.Iterations)
          // .strength(defaultForceConfig.link.Strength)
        )
        .force(
          "charge",
          d3
            .forceManyBody()
            .strength(function (d) {
              //console.log(d.showDetail);
              let strength = that.circleStrength;
              if (d.showDetail) {
                strength = that.vegaLiteStrength;
              } else {
                if (that.showIndex.size > 0) {
                  const id = d.id.replace(".", "");
                  for (const index of that.showIndex.keys()) {
                    const showId = nodes[index].id.replace(".", "");
                    const directNeighbor = that.neighborMap.get(showId);
                    if (directNeighbor) {
                      for (const neighbor of directNeighbor) {
                        const secondNeighbor = that.neighborMap.get(neighbor);
                        if (secondNeighbor.includes(id)) {
                          return that.circleNeighborStrength;
                        }
                      }
                    }
                  }
                }
              }

              return strength;
            })
            .theta(defaultForceConfig.manyBody.Theta)
            .distanceMin(defaultForceConfig.manyBody.DistanceMin)
          // .distanceMax(defaultForceConfig.manyBody.DistanceMax)
        )
        .force(
          "center",
          d3
            .forceCenter(width / 2, height / 2)
            .strength(defaultForceConfig.center.Strength)
        )
        .force(
          "x",

          d3
            .forceX()
            .x(width / 2)
            .strength(defaultForceConfig.x.Strength)
        )
        .force(
          "y",

          d3
            .forceY()
            .y(height / 2)
            .strength(defaultForceConfig.y.Strength)
        )
        .force(
          "collide",
          d3
            .forceCollide((d) => {
              if (d.showDetail) {
                return d.rect.r;
              } else {
                return that.circleR;
              }
            })
            .strength(defaultForceConfig.collide.Strength)
            .iterations(defaultForceConfig.collide.Iterations)
        )
        .alpha(defaultBaseConfig.alpha)
        .alphaMin(defaultBaseConfig.alphaMin)
        .alphaTarget(defaultBaseConfig.alphaTarget)
        .alphaDecay(defaultBaseConfig.alphaDecay)
        .velocityDecay(defaultBaseConfig.velocityDecay)
        .on("tick", ticked);

      // 每次迭代回调函数，更新结点位置
      function ticked() {
        that.ticks++;

        // 只通过transform.translate 更新父元素g的位置
        containerGroup.style("transform", (d) => {
          let offsetWidth = 0;
          let offsetHeight = 0;

          if (d.showDetail) {
            offsetWidth =
              d.img.width / 2 + that.rectWidthOffset + that.iconOffset;
            offsetHeight =
              d.img.height / 2 +
              ((that.rectHeightOffset + that.iconOffset) * 5) / 4;
          } else {
            offsetWidth = offsetHeight = that.circleR;
          }
          const x = d.x;
          const y = d.y;
          if (x - offsetWidth < that.leftCornerCoord[0]) {
            // d.vx = Math.abs(d.vx);
            d.x = that.leftCornerCoord[0] + offsetWidth;
          } else if (x + offsetWidth > that.rightCornerCoord[0]) {
            //d.vx = -Math.abs(d.vx);
            d.x = that.rightCornerCoord[0] - offsetWidth;
          }

          if (y - offsetHeight < that.leftCornerCoord[1]) {
            // d.vy = Math.abs(d.vy);
            d.y = that.leftCornerCoord[1] + offsetHeight;
          } else if (y + offsetHeight > that.rightCornerCoord[1]) {
            //  d.vy = -Math.abs(d.vy);
            d.y = that.rightCornerCoord[1] - offsetHeight;
          }
          return `translate(${d.x}px,${d.y}px)`;
        });

        linkGroup
          .attr("x1", (d) => d.source.x)
          .attr("y1", (d) => d.source.y)
          .attr("x2", (d) => d.target.x)
          .attr("y2", (d) => d.target.y);
      }

      const nodeG = svg.selectChild(".node-group");

      const dragDefine = d3
        .drag()
        .container(function () {
          // 选择顶层nodeGy元素作为容器，影响 event.x和event.y
          return nodeG.node();
        })
        .subject(function (event) {
          // 将父元素 g 作为 subject 返回 (因为数据挂载在父元素g上)
          return d3.select(this.parentNode).datum();
        })
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
      // 设置结点拖动行为，也是只在圆上设置，避免与vega-lite图的鼠标事件冲突
      circleGroup.call(dragDefine);
      rectGroup.call(dragDefine);

      // 拖动开始时，重新加热迭代过程，并且修正被拖动点的fx,fy
      function dragstarted(event) {
        if (!event.active)
          simulation
            .alphaTarget(
              +that.alphaTarget + 0.3 > 1 ? 1 : +that.alphaTarget + 0.3
            )
            .restart();

        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
      }

      // 拖动时，让点跟着鼠标走
      function dragged(event) {
        // 更新节点位置
        event.subject.fx = event.x;
        event.subject.fy = event.y;
      }

      // 拖动结束，降温
      function dragended(event) {
        if (!event.active) simulation.alphaTarget(that.alphaTarget);

        if (event.subject.pinned) {
          event.subject.fx = event.subject.x;
          event.subject.fy = event.subject.y;
        } else {
          event.subject.fx = null;
          event.subject.fy = null;
        }
      }

      // 设置整体zoom行为,只选择最顶层的2个g即可
      const group = svg.selectChildren("g");

      //console.log(group);
      // 创建缩放函数
      const zoom = d3
        .zoom()
        .scaleExtent([0.5, 30]) // 设置缩放的范围
        .translateExtent([
          [0, 0],
          [width, height],
        ])
        .on("zoom", zoomed)
        // .on("end", zoomEnd)
        .filter((event) => event.target === svg.node());

      // 仅将缩放行为应用到顶层元素
      svg.call(zoom);
      // 定义zoom的回调函数
      function zoomed(event) {
        const transform = event.transform;
        //console.log(that.transform);
        // 更新地理路径组的变换属性
        group.attr("transform", transform);
        //    console.log(transform);
        if (transform.k < 1.3) {
          that.leftCornerCoord = transform.invert([0, 0]);
          that.rightCornerCoord = transform.invert([width, height]);
        }
      }

      // initialize the default data
      // this.diagonal = diagonal;
      this.simulation = simulation;
      this.centerX =
        this.defaultForceConfig.center.X =
        this.xX =
        this.defaultForceConfig.x.X =
        this.radialX =
        this.defaultForceConfig.radial.X =
          width / 2;
      this.centerY =
        this.defaultForceConfig.center.Y =
        this.yY =
        this.defaultForceConfig.y.Y =
        this.radialY =
        this.defaultForceConfig.radial.Y =
          height / 2;
      this.defaultForceConfig.collide.Radius = this.collideRadius =
        this.circleR;

      function togglePin(event, d) {
        const g = d3.select(this.parentNode);
        const pinned = !g.datum().pinned;
        g.datum().pinned = pinned;
        g.classed("pinned", true);
        if (pinned) {
          g.datum().fx = g.datum().x;
          g.datum().fy = g.datum().y;
          g.select(".pin").classed("icon-pinned", true);

          that.drawVegaLite(g, d.index, "svg");
        } else {
          g.classed("pinned", false);
          g.select(".pin").classed("icon-pinned", false);
          g.datum().fx = null;
          g.datum().fy = null;

          that.drawVegaLite(g, d.index, "img");
        }
      }
    },
  },

  created() {
    this.loadData();
  },
};
</script>

<style scoped>
.container {
  height: 100%;
  width: 100%;
  position: relative;
  overflow: hidden;
}
#svg-container {
  height: 100%;
  width: 100%;
}

.edit-panel {
  position: absolute;
  top: 5%;
  left: 1%;
  z-index: 10;
  height: 90%;
  overflow: auto;
}
.edit-panel:not(.el-menu--collapse) {
  width: 200px;
}

/* scroll bar hide */
.edit-panel {
  -ms-overflow-style: none; /* Internet Explorer 10+ */
  scrollbar-width: none; /* Firefox */
}
.edit-panel::-webkit-scrollbar {
  display: none; /* Safari and Chrome */
}

.edit-btn {
  position: fixed;
  bottom: 5%;
  right: 3%;
}

.ticks-card {
  position: fixed;
  top: 5%;
  right: 3%;
  padding: 1vw;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.active-btn {
  box-shadow: inset 2px 2px 16px #4444442a, inset -2px -2px 16px #4444442a;
}

.btn {
  border-radius: 12px;
}
</style>

<!-- Animation -->
<style scoped>
.slide-enter-active {
  transition: all 0.3s ease-out;
}

.slide-leave-active {
  transition: all 0.3s ease-in;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateX(-200px); /* 初始状态和最终状态 */
}

.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translateX(0); /* 平移隐藏 */
}
</style>

<!-- form -->
<style scoped>
.el-menu-item {
  height: fit-content;
}
.form {
  padding: 0.8vw 2vw 1vw 2vw;
}

.form-item-control {
  margin-bottom: 10px;
}
.config-btn {
  font-size: 100%;
  flex: 1 1 50%;
}

.form-btn-control {
  display: flex;
  gap: 0.5vw;
  width: 100%;
}
.btn-label {
  width: 85%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.input-control {
  /* width: 90%; */
}
</style>

<style lang="less" scoped>
.el-slider {
  width: 100%;
}
.bugfix {
  margin-top: 10px;
}
</style>

<!-- global style -->
<style scoped lang="less">
.circle,
.rect,
.network-line,
.rect-title {
  &.hover-highlight {
    stroke: #b197fc;
    stroke-width: 3px;
  }
  &.selected-highlight {
    stroke: #22b8cf;
    stroke-width: 3px;
  }
  &.center-highlight {
    stroke: #0c8599;
    stroke-width: 3px;
  }
}

.el-form-item__label {
  margin-bottom: 2px !important;
}
.el-tabs__content {
  display: flex;
  align-items: center;
}

.pinned {
  will-change: transform;
}

.not-show {
  display: none;
}

.vega-lite-icon {
  fill: #555;
}
.vega-lite-icon:hover,
.vega-lite-icon:active {
  fill: #22b8cf;
}
.icon-pinned {
  fill: #1098ad;
}
</style>
