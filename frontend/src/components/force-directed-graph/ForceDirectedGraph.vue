<template>
  <div class="container">
    <transition name="slide">
      <div class="more-box" v-show="showMoreIcon">
        <svg
          class="more-icon"
          viewBox="0 0 1024 1024"
          xmlns="http://www.w3.org/2000/svg"
          @click="
            showMoreIcon = !showMoreIcon;
            showMorePanel = !showMorePanel;
            hidePanelMode = !hidePanelMode;
          "
        >
          <path
            d="M511.48 22.62c-270.42 0-489.62 218.96-489.62 489.09s219.2 489.09 489.62 489.09 489.61-218.96 489.61-489.09S781.89 22.62 511.48 22.62zM211.83 435.56c-0.11-0.19-0.11-0.49-0.23-0.71l-0.3-1.2c0-0.23-0.11-0.42-0.11-0.6l-0.3-1.32c0-0.3-0.11-0.49-0.11-0.68-0.08-0.42-0.08-0.94-0.19-1.32 0-0.3-0.12-0.53-0.12-0.83 0-0.37-0.11-0.79-0.11-1.2-0.07-0.26-0.07-0.68-0.07-1.01v0.04c0-0.3-0.11-0.6 0-1.13-0.11-0.6-0.11-1.32-0.11-2 0-0.71 0.11-1.32 0.11-2.03l0.07-0.98 0.11-1.02c0-0.41 0-0.83 0.12-1.2 0-0.3 0.11-0.53 0.11-0.83 0.01-0.43 0.08-0.86 0.19-1.28 0-0.34 0.11-0.53 0.11-0.71l0.3-1.31c0-0.23 0-0.42 0.11-0.6l0.3-1.2c0.11-0.19 0.11-0.49 0.22-0.68 0.07-0.34 0.3-0.75 0.41-1.13l0.3-0.83c0.11-0.3 0.3-0.68 0.38-0.98l0.38-0.9c0.07-0.3 0.26-0.6 0.37-0.91 0.08-0.3 0.23-0.71 0.45-1.02 0.19-0.22 0.26-0.53 0.38-0.68 0.11-0.45 0.3-0.75 0.53-1.13 0.17-0.17 0.31-0.38 0.41-0.6 0.19-0.42 0.42-0.71 0.64-1.13 0.16-0.17 0.28-0.36 0.38-0.56 0.22-0.42 0.53-0.75 0.75-1.13 0.08-0.22 0.3-0.42 0.42-0.6l0.83-1.13 0.49-0.6c0.23-0.3 0.41-0.6 0.72-0.9 0.22-0.3 0.53-0.49 0.75-0.79 0.22-0.19 0.42-0.53 0.6-0.71l1.47-1.51 99.24-96.46c16.73-16.11 43.23-16.11 59.96 0 16.57 16.1 16.57 42.14 0 58.24l-26.93 26.15h413.09c23.5 0 42.44 18.51 42.44 41.23 0 22.84-19.06 41.27-42.44 41.27H252.39c-0.6 0-1.32-0.12-2.07-0.12l-0.9-0.11-1.06-0.07c-0.42 0.01-0.84-0.02-1.24-0.11-0.3 0-0.53-0.11-0.83-0.11-0.44-0.02-0.89-0.08-1.32-0.19-0.34 0-0.53-0.11-0.76-0.11l-1.32-0.3c-0.34-0.08-0.53-0.08-0.75-0.19l-1.2-0.3c-0.23-0.11-0.56-0.11-0.76-0.23l-1.13-0.37-0.83-0.34-1.06-0.38-0.9-0.3-0.94-0.42c-0.3-0.08-0.71-0.19-1.02-0.42-0.22-0.19-0.53-0.26-0.75-0.37-0.38-0.11-0.76-0.3-1.13-0.53-0.19-0.16-0.41-0.29-0.64-0.38l-1.13-0.6c-0.19-0.16-0.41-0.29-0.64-0.37-0.38-0.23-0.72-0.53-1.13-0.76-0.23-0.08-0.41-0.3-0.6-0.37l-1.13-0.83-0.64-0.45-0.94-0.75c-0.3-0.19-0.49-0.49-0.79-0.68l-0.75-0.6c-0.49-0.53-1.02-0.91-1.55-1.43-0.53-0.49-0.94-1.02-1.43-1.5-0.22-0.19-0.42-0.49-0.6-0.72-0.23-0.3-0.57-0.49-0.75-0.79-0.23-0.3-0.53-0.6-0.72-0.91l-0.53-0.6c-0.3-0.37-0.64-0.71-0.86-1.13-0.07-0.19-0.27-0.37-0.38-0.56-0.22-0.41-0.53-0.75-0.75-1.13-0.19-0.22-0.3-0.41-0.38-0.6l-0.64-1.09-0.41-0.64c-0.11-0.37-0.3-0.68-0.53-1.05-0.19-0.22-0.3-0.52-0.41-0.75-0.07-0.3-0.3-0.68-0.41-0.98-0.08-0.3-0.3-0.6-0.42-0.9l-0.3-0.94-0.42-1.02-0.3-0.75c-0.22-0.35-0.3-0.76-0.41-1.14z m600.83 166.18l-0.07 1.02-0.11 1.02c0 0.38 0 0.79-0.11 1.2 0 0.3-0.12 0.49-0.12 0.79-0.01 0.44-0.08 0.89-0.19 1.32 0 0.3-0.11 0.49-0.11 0.68l-0.3 1.32c0 0.23 0 0.41-0.11 0.6l-0.3 1.2c-0.12 0.23-0.12 0.53-0.23 0.72-0.08 0.34-0.3 0.71-0.41 1.09-0.08 0.34-0.19 0.53-0.3 0.83l-0.38 1.02-0.37 0.9c-0.07 0.3-0.27 0.61-0.38 0.91-0.08 0.3-0.22 0.68-0.45 0.98-0.19 0.22-0.26 0.53-0.37 0.71-0.12 0.38-0.3 0.71-0.53 1.13-0.19 0.19-0.3 0.38-0.42 0.56-0.19 0.41-0.41 0.75-0.64 1.13-0.19 0.22-0.3 0.42-0.38 0.6-0.22 0.38-0.53 0.71-0.75 1.13-0.08 0.19-0.3 0.38-0.42 0.56-0.3 0.41-0.49 0.75-0.83 1.13l-0.49 0.6c-0.23 0.3-0.42 0.6-0.76 0.91-0.3 0.3-0.49 0.6-0.83 0.9-0.22 0.19-0.41 0.53-0.6 0.71l-1.47 1.51-99.28 96.46c-16.53 16.1-43.31 16.1-59.88 0s-16.57-42.14 0-58.24l26.89-26.15h-413.2c-23.46 0-42.41-18.51-42.41-41.23 0-22.84 19.06-41.27 42.41-41.27h515.68c0.6 0 1.32 0.11 2.07 0.11 0.3 0 0.6 0.11 0.94 0.11l1.02 0.08c0.42 0 0.87 0 1.24 0.11 0.3 0 0.53 0.12 0.83 0.12 0.44 0.01 0.89 0.08 1.32 0.19 0.38 0 0.57 0.11 0.76 0.11l1.32 0.3c0.37 0.07 0.56 0.07 0.75 0.19l1.24 0.3c0.23 0.12 0.53 0.12 0.76 0.23l1.13 0.37 0.79 0.34 1.06 0.38 0.94 0.3 0.9 0.41c0.34 0.08 0.75 0.19 1.02 0.42 0.22 0.19 0.57 0.26 0.75 0.37 0.42 0.12 0.76 0.3 1.13 0.53 0.19 0.16 0.41 0.29 0.64 0.38l1.13 0.6c0.23 0.19 0.41 0.3 0.64 0.38 0.38 0.22 0.72 0.53 1.13 0.75 0.19 0.08 0.42 0.3 0.64 0.38l1.13 0.83 0.61 0.45c0.3 0.22 0.64 0.45 0.94 0.75 0.3 0.19 0.53 0.49 0.79 0.68l0.75 0.6 1.55 1.43 1.47 1.51c0.23 0.19 0.42 0.49 0.6 0.71 0.23 0.3 0.53 0.49 0.71 0.79l0.76 0.91 0.49 0.6c0.34 0.38 0.64 0.71 0.86 1.13 0.08 0.19 0.3 0.38 0.38 0.56 0.22 0.42 0.53 0.75 0.75 1.13 0.17 0.17 0.31 0.38 0.41 0.6 0.19 0.42 0.42 0.71 0.64 1.09 0.19 0.22 0.26 0.42 0.38 0.64 0.11 0.38 0.3 0.68 0.53 1.05 0.19 0.22 0.3 0.53 0.41 0.75l0.42 0.98c0.11 0.3 0.3 0.6 0.38 0.9l0.37 0.94 0.38 1.02 0.34 0.75c0.19 0.35 0.31 0.73 0.37 1.13 0.11 0.19 0.11 0.49 0.23 0.71l0.3 1.2c0 0.23 0 0.41 0.11 0.61l0.3 1.32c0 0.3 0.11 0.49 0.11 0.68 0.11 0.42 0.11 0.94 0.19 1.32 0 0.3 0.12 0.53 0.12 0.83 0 0.37 0.11 0.79 0.11 1.2 0.11 0.3 0.11 0.68 0.11 0.98 0.07 0.41 0.07 0.71 0.07 1.01 0.11 0.6 0.11 1.28 0.11 2.03 0.01 0.66-0.11 1.26-0.11 1.97z"
          ></path>
        </svg>
      </div>
    </transition>
    <transition name="slide">
      <VegaLiteFilter
        v-if="showMorePanel"
        :insightList="filterNode['insight-list']"
        :insightIndex="filterNode['insightIndex']"
        class="showMorePanelBox"
        @insightIndexChange="changeInsightIndex"
        @hideMoreBox="hideMoreBox"
      ></VegaLiteFilter>
    </transition>

    <div id="force-svg-container">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        id="total-svg"
        style="width: 100%; height: 100%; user-select: none"
      >
        <defs>
          <filter
            id="inset-shadow"
            x="-50%"
            y="-50%"
            width="200%"
            height="200%"
          >
            <feComponentTransfer in="SourceAlpha">
              <feFuncA type="table" tableValues="1 0"></feFuncA>
            </feComponentTransfer>
            <feGaussianBlur stdDeviation="5"></feGaussianBlur>
            <feOffset dx="2.5" dy="2.5" result="offsetblur"></feOffset>
            <feFlood flood-color="steelblue" result="color"></feFlood>
            <feComposite in2="offsetblur" operator="in"></feComposite>
            <feComposite in2="SourceAlpha" operator="in"></feComposite>
            <feMerge>
              <feMergeNode in="SourceGraphic"></feMergeNode>
              <feMergeNode></feMergeNode>
            </feMerge>
          </filter>

          <filter
            id="inset-shadow-circle"
            x="-50%"
            y="-50%"
            width="200%"
            height="200%"
          >
            <feComponentTransfer in="SourceAlpha">
              <feFuncA type="table" tableValues="1 0"></feFuncA>
            </feComponentTransfer>
            <feGaussianBlur stdDeviation="6"></feGaussianBlur>
            <feOffset dx="0" dy="0" result="offsetblur"></feOffset>
            <feFlood flood-color="#545b77" result="color"></feFlood>
            <feComposite in2="offsetblur" operator="in"></feComposite>
            <feComposite in2="SourceAlpha" operator="in"></feComposite>
            <feMerge>
              <feMergeNode in="SourceGraphic"></feMergeNode>
              <feMergeNode></feMergeNode>
            </feMerge>
          </filter>
          <filter id="rect-shadow">
            <feDropShadow
              dx="2"
              dy="2"
              stdDeviation="4"
              flood-color="#545b77"
              flood-opacity="0.5"
            />
          </filter>
          <filter id="rect-shadow-focus">
            <feOffset in="SourceAlpha" dx="0" dy="0" result="offsetAlpha" />
            <feMorphology
              in="offsetAlpha"
              operator="dilate"
              radius="2.5"
              result="morphedAlpha"
            />
            <feGaussianBlur
              in="morphedAlpha"
              stdDeviation="6"
              result="blurAlpha"
            />
            <feFlood
              flood-color="#545b77"
              flood-opacity="0.8"
              result="floodColor"
            />
            <feComposite
              in="floodColor"
              in2="blurAlpha"
              operator="in"
              result="colorBlur"
            />
            <feMerge>
              <feMergeNode in="colorBlur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
          <symbol
            id="defs-dominance"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/dominance.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-outlier"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/outlier.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-top2"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/top2.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-evenness"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/evenness.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-trend"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/trend.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-skewness"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/skewness.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-kurtosis"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/kurtosis.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-correlation"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/correlation.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-outlier-temporal"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
          >
            <image
              href="/pic/outlier-temporal.png"
              :width="insightIconSize"
              :height="insightIconSize"
            ></image>
          </symbol>
          <symbol
            id="defs-focus"
            viewBox="0 0 1024 1024"
            xmlns="http://www.w3.org/2000/svg"
          >
            <svg viewBox="0 0 1024 1024" width="100%" height="100%">
              <rect
                width="100%"
                height="100%"
                stroke="none"
                rx="10%"
                fill="currentcolor"
              ></rect>
              <path
                d="M882.816 474.944h-33.92c-18.336-151.584-139.36-272.096-292.544-291.296V150.784c0-22.816-18.304-41.088-40.32-41.088-22.912 0-41.248 18.272-41.248 41.088v32.864c-152.224 19.2-273.248 139.712-292.512 291.296H149.28c-22.944 0-41.28 18.24-41.28 41.088 0 21.888 18.336 40.16 41.28 40.16h32.992c19.264 152.48 140.288 272.992 292.512 291.264v33.824c0 21.92 18.336 40.16 41.248 40.16 22.016 0 40.32-18.24 40.32-40.16v-33.824c153.152-18.24 274.176-138.784 292.544-291.264h33.92a40.64 40.64 0 0 0 40.352-40.16c0-22.848-18.336-41.088-40.352-41.088z m-116.448 0h-105.472a152.96 152.96 0 0 0-104.544-104.096V266.752c107.328 17.344 192.576 101.344 210.016 208.192z m-291.584-208.224v104.096a153.248 153.248 0 0 0-104.544 104.096H265.728a252.672 252.672 0 0 1 209.056-208.192z m-209.024 289.472h104.512a153.248 153.248 0 0 0 104.544 104.096v104.992a253.6 253.6 0 0 1-209.056-209.088z m290.624 209.088v-104.992a153.12 153.12 0 0 0 104.544-104.096h105.472c-17.472 106.816-102.72 191.712-210.016 209.088z"
              ></path>
            </svg>
          </symbol>
          <symbol
            id="defs-amplify"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
            xmlns="http://www.w3.org/2000/svg"
          >
            <svg viewBox="0 0 1024 1024" width="100%" height="100%">
              <rect
                width="100%"
                height="100%"
                stroke="none"
                rx="10%"
                fill="currentcolor"
              ></rect>
              <path
                d="M852.68743 966.232318 171.311547 966.232318c-62.714867 0-113.562988-50.846038-113.562988-113.558335L57.748558 171.324994c0-62.712297 50.848122-113.558335 113.562988-113.558335l681.376907 0c62.714867 0 113.562988 50.846038 113.562988 113.558335l0 681.348989C966.250418 915.38628 915.40332 966.232318 852.68743 966.232318zM909.469948 171.324994c0-31.356149-25.424061-56.779168-56.781494-56.779168L171.311547 114.545826c-31.357433 0-56.781494 25.423019-56.781494 56.779168l0 681.348989c0 31.357172 25.424061 56.779168 56.781494 56.779168l681.376907 0c31.358457 0 56.781494-25.423019 56.781494-56.779168L909.469948 171.324994zM824.297706 483.610416c-15.665413 0-28.390747-12.697183-28.390747-28.389584l0.887243-186.638771L604.102866 461.264479l-40.145947-40.144302 193.023924-193.016015L568.782006 228.104161c-15.693044 0-28.390747-12.697183-28.390747-28.389584s12.697704-28.389584 28.390747-28.389584l254.711349 0c7.929925 0 15.082105 3.27151 20.238756 8.53949 5.490263 4.657067 8.955319 11.449773 8.955319 19.850094l0 255.506255C852.68743 470.913233 839.989727 483.610416 824.297706 483.610416zM455.219017 852.673983 200.506645 852.673983c-7.929925 0-15.082105-3.270487-20.239779-8.538467-5.489239-4.65809-8.955319-11.423167-8.955319-19.850094L171.311547 568.779168c0-15.692401 12.726357-28.389584 28.390747-28.389584 15.69202 0 28.390747 12.697183 28.390747 28.389584l-0.887243 186.6664 192.690312-192.710047 40.173577 40.143279-193.050531 193.016015 188.198837 0c15.69202 0 28.390747 12.697183 28.390747 28.389584C483.608741 839.9768 470.911038 852.673983 455.219017 852.673983z"
              ></path>
            </svg>
          </symbol>
          <symbol
            id="defs-back"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
            xmlns="http://www.w3.org/2000/svg"
          >
            <svg viewBox="0 0 1024 1024" width="100%" height="100%">
              <rect
                width="100%"
                height="100%"
                stroke="none"
                rx="10%"
                fill="currentcolor"
              ></rect>
              <path
                d="M471.893333 149.333333a42.666667 42.666667 0 0 0-73.258666-29.781333l-343.893334 352.981333a42.666667 42.666667 0 0 0-0.768 58.709334l343.893334 372.352a42.666667 42.666667 0 0 0 73.984-28.928v-190.677334c56.917333-5.248 116.821333-1.365333 179.882666 11.989334 65.834667 13.994667 150.528 76.032 253.909334 202.24a42.666667 42.666667 0 0 0 75.477333-31.36c-15.445333-152.32-73.984-281.301333-176.170667-384.853334-92.757333-93.994667-204.373333-146.432-333.098666-156.586666V149.333333z"
              ></path>
            </svg>
          </symbol>
          <symbol
            id="defs-shrink"
            :viewBox="`0 0 ${insightIconSize} ${insightIconSize}`"
            xmlns="http://www.w3.org/2000/svg"
          >
            <svg viewBox="0 0 1024 1024" width="100%" height="100%">
              <rect
                width="100%"
                height="100%"
                stroke="none"
                rx="10%"
                fill="currentcolor"
              ></rect>
              <path
                d="M476.936925 546.649148c-4.836145-4.926196-11.531638-8.014534-18.98233-8.014534l-239.052514 0.010233c-14.71412 0-26.644847 11.92561-26.644847 26.643823 0 14.72026 11.930727 26.637684 26.644847 26.637684l176.615487 0L214.360647 773.084297l37.682227 37.686321 180.862207-180.863231-0.841158 175.191044c0 14.70798 11.929704 26.643823 26.644847 26.643823s26.64587-11.935843 26.64587-26.643823L485.354642 565.28867C485.354642 557.388746 482.088248 551.022759 476.936925 546.649148zM831.741743 85.676311l-639.48451 0c-58.862619 0-106.58041 47.712675-106.58041 106.58041l0 639.485533c0 58.867736 47.717791 106.581434 106.58041 106.581434l639.48451 0c58.863642 0 106.581434-47.713698 106.581434-106.581434L938.323177 192.256722C938.323177 133.388986 890.605386 85.676311 831.741743 85.676311zM885.031437 831.742255c0 29.430286-23.856337 53.289694-53.289694 53.289694l-639.48451 0c-29.429263 0-53.290717-23.859407-53.290717-53.289694L138.966517 192.256722c0-29.437449 23.861454-53.290717 53.290717-53.290717l639.48451 0c29.434379 0 53.289694 23.853267 53.289694 53.290717L885.031437 831.742255zM805.09792 432.063413l-176.62265 0.008186L809.638329 250.907517l-37.684274-37.678134-180.859138 180.861184 0.841158-175.188998c0-14.719236-11.93175-26.644847-26.647917-26.644847-14.712073 0-26.643823 11.92561-26.643823 26.644847l0 239.807714c0 7.892761 3.2623 14.259772 8.414647 18.639522 4.835122 4.927219 11.535731 8.015557 18.987447 8.015557l239.051491-0.00921c14.718213 0 26.643823-11.93482 26.643823-26.644847C831.741743 443.990047 819.816133 432.063413 805.09792 432.063413z"
              ></path>
            </svg>
          </symbol>
        </defs>
      </svg>
    </div>

    <defs style="display: none">
      <svg
        viewBox="0 0 1024 1024"
        xmlns="http://www.w3.org/2000/svg"
        id="defs-remove"
        :width="iconSize"
        :height="iconSize"
      >
        <rect
          width="100%"
          height="100%"
          stroke="none"
          fill="transparent"
        ></rect>
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
        <rect
          width="100%"
          height="100%"
          stroke="none"
          fill="transparent"
        ></rect>
        <path
          d="M320 839.68l-238.592 174.08c-8.704 6.656-19.456 9.728-29.696 9.728-12.8 0-26.112-5.12-35.84-14.848-17.92-17.92-20.48-46.08-5.12-66.56l212.992-288.256L56.32 487.424C39.936 471.04 36.864 445.44 48.128 425.472c8.192-12.8 76.8-112.64 229.376-75.264 2.56 0.512 5.12 0.512 8.192 1.024 6.144 0.512 13.312 1.024 20.992 2.56 32.256 5.12 89.6-20.48 139.264-62.976 47.616-40.448 78.336-87.552 78.336-120.32 0-7.68 0-15.872-0.512-23.552-1.024-30.72-3.072-77.824 31.744-112.64 41.472-41.472 107.52-45.056 153.088-7.68 1.024 0.512 1.536 1.536 2.56 2.56 24.576 24.064 276.48 275.968 279.04 278.528 21.504 21.504 33.792 50.688 33.792 81.408s-11.776 59.392-33.792 80.896c-34.816 34.816-82.432 33.28-113.664 31.744-7.168 0-15.36-0.512-23.04-0.512-30.72 0-67.584 21.504-103.936 60.928-50.688 55.296-81.92 126.464-79.36 158.72 1.024 10.24 3.072 28.16 3.584 30.72 36.864 149.504-62.976 217.6-74.752 225.28-20.48 12.288-46.592 9.216-62.976-7.168l-165.376-165.376-50.688 35.328z"
        ></path>
      </svg>
      <svg
        id="defs-check"
        viewBox="0 0 1024 1024"
        xmlns="http://www.w3.org/2000/svg"
        :width="iconSize"
        :height="iconSize"
      >
        <rect
          width="100%"
          height="100%"
          stroke="none"
          fill="transparent"
        ></rect>
        <path
          d="M1002.88 321.92L405.76 935.04a32 32 0 0 1-45.76 0L21.12 612.48a32 32 0 0 1 0-44.8L160 433.6a32 32 0 0 1 45.76 0L359.04 576 796.16 120.64a32 32 0 0 1 46.08 0l160 156.48a32 32 0 0 1 0.64 44.8z"
        ></path>
      </svg>
      <!-- insight icon -->
    </defs>
  </div>
</template>

<script>
import VegaLiteFilter from "@/components/force-directed-graph/VegaLiteFilter.vue";

export default {
  components: {
    VegaLiteFilter,
  },

  computed: {
    selectedData() {
      return this.$store.getters["force/selectedData"];
    },
    allStatesData() {
      return this.$store.getters["force/allStatesData"];
    },
    stateLinksMap() {
      return this.$store.getters["force/stateLinksMap"];
    },
    scoreSelectionMaps() {
      return this.$store.getters["force/scoreSelectionMaps"];
    },
  },

  data() {
    return {
      // data reload
      refreshFlag: true,
      // tree info
      exploredPaths: new Map(),

      // svg 状态切换相关
      amplifyMode: false,
      backMode: false,
      firstUpdateFlag: true,
      // vega-lite filter
      filterNode: {
        id: null,
        state: null,
        insightIndex: null,
        "insight-list": null,
      },
      // top svg force control
      maxNodeNum: 0,
      svgViewBoxScale: null,
      svgRScale: null,
      linkDistanceScale: null,
      chargeStrengthScale: null,
      containerWidth: null,
      containerHeight: null,

      // mutiple states
      focusState: "S0",
      oldFocusState: null,
      selectedNodes: new Map(),
      checkIndexs: new Map(),
      hoverIndexs: new Map(),
      showIndexs: new Map(),
      pinnedIndexs: new Map(),
      simulations: new Map(),
      // 都是“当前状态下” 传来数据的索引，重复值只在focus state中出现
      neighborMaps: new Map(), // (id, gdata)
      // nodeIdMaps 在每次 drawGraph 和 drawSubGraph 中都会更新，保持总是记录的是被力导图控制的点
      // 受nodeStateMaps的更新规律影响，也是总是记录的"最大"的nodes数
      nodeIdMaps: new Map(),
      circleRScales: new Map(),
      insightSizeScales: new Map(),
      selectedIds: new Map(),
      zooms: new Map(),
      //
      oldFoucsStateLinksMaps: new Map(),

      selectedDatas: new Map(),
      svgNodeDatas: new Map(),
      svgLinkDatas: [],
      globalBundleData: [],
      preservedBundleData: [],
      pathStack: [],
      focusedStates: new Set(),

      // 原始数据
      // 回退不更新，focus过的不更新 （记录的是较大值，但是较小值的情况下会重复更新）
      linkStateMaps: new Map(),
      nodeStateMaps: new Map(),
      // 累计的 nodeIdMaps
      // 记录的是每个state“最大”的原始数据
      originNodeIdMaps: new Map(),
      showStateList: [],
      newStateList: [],

      crossStatesHoveredNeighbor: null,
      globalSimulation: null,
      globalDragDefine: null,

      // focus control
      // (id,view)
      showIndex: new Map(),
      // (id, g)
      pinnedIndex: new Map(),
      // (id, row, col)
      checkIndex: new Map(),
      // (id, row,col)
      hoverIndex: {
        id: null,
        row: null,
        col: null,
      },
      // id
      selectedNode: {
        id: null,
        state: null,
        insightIndex: null,
        "insight-list": null,
        col: null,
        row: null,
      },

      // color
      defaultLinkColor: "#999",
      defaultNodeColor: "#aaa",
      circleHoveredColor: "#e6fcf5",
      nodeTypeColor: null,

      circleRScale: null,
      insightSizeScale: null,

      circleR: 14,
      circleFocusR: 28,
      // rectWH: 125 * 0.7 + 20,
      rectWidthOffset: 3,
      rectHeightOffset: 13,
      rectHeightBottomOffset: 3,
      rectR: 10,
      vegaLiteR: 125,
      vegaLiteHeight: 100,
      vegaLiteWidth: 150,

      circleLink: 30,
      vegaLiteLink: 200,
      vegaLiteLongLink: 350,
      circleNeighborLink: 100,

      circleStrength: -250,
      circleNeighborStrength: -500,
      vegaLiteStrength: -3000,

      insightNum: 7,
      insightIconSize: 20,
      iconSize: 15,
      iconOffset: 5,

      // showMoreIcon
      showMoreIcon: false,
      showMorePanel: false,
      hidePanelMode: false,

      editMode: false,
      durationTime: 150,

      /* -------------------------------------------------------------------------- */
      // force Config
      restartAlphaDecay: 1 - Math.pow(0.001, 1 / 300),
      defaultBaseConfig: {
        alpha: 1,
        alphaMin: 0.001,
        alphaDecay: 1 - Math.pow(0.001, 1 / 300),
        alphaTarget: 0,
        velocityDecay: 0.4,
      },

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
        collide: {
          Radius: null,
          Strength: 1,
          Iterations: 1,
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
      },
    };
  },

  watch: {
    crossStatesHoveredNeighbor(newVal, oldVal) {
      if (newVal) {
        Array.from(newVal.keys()).forEach((state) => {
          this.crossStatesNeighborHighlight(newVal.get(state), true, state);
        });
      }
      if (oldVal) {
        Array.from(oldVal.keys()).forEach((state) => {
          this.crossStatesNeighborHighlight(oldVal.get(state), false, state);
        });
      }
    },
    // showIndex: {
    //   deep: true,
    //   handler(newVal) {},
    // },
    allStatesData: {
      // don't watch deep
      handler(newVal, oldVal) {
        // 记录 links和nodes原始数据
        if (!this.backMode)
          for (const [state, value] of newVal.entries()) {
            if (!this.focusedStates.has(state)) {
              this.linkStateMaps.set(state, value.links);
              this.nodeStateMaps.set(state, value.nodes);
            }
          }
        this.firstUpdateFlag = true;

        if (oldVal) {
          if (newVal) {
            if (this.backMode) {
              const newOldFocusInfo = this.pathStack.pop();

              this.preservedBundleData = newOldFocusInfo.bundleData;

              const oldNewStates = this.newStateList;
              const oldShowStates = this.showStateList;

              const preservedStates = oldShowStates.filter(
                (state) => !oldNewStates.includes(state)
              );

              const newAddedStates = Array.from(newVal.keys()).filter(
                (state) => !preservedStates.includes(state)
              );
              const showStateList = [
                ...new Set(preservedStates.concat(Array.from(newVal.keys()))),
              ];
              // 本状态下，需要刷新bundle的state，这里的newStates会有 old focus state，且不包含回退后的“new old focus state”
              const newStates = Array.from(newVal.keys()).filter(
                (state) => state !== this.focusState
              );

              // 更新全局state 信息
              this.showStateList = showStateList;
              this.newStateList = newStates;
              // 更新全局svg dom元素
              const [newSvgData, newLinkData] = this.updateGlobalDom(
                showStateList,
                newAddedStates,
                oldNewStates,
                true,
                newOldFocusInfo.state
              );

              this.svgLinkDatas = newLinkData;
              this.updateOldFocusState(this.oldFocusState, true);
              this.addNewState(newAddedStates);

              this.oldFocusState = newOldFocusInfo.state;

              this.updateNewFocusState(this.focusState, true);

              this.updateGlobalForce(newSvgData, newLinkData);
            } else {
              // update

              // 获取需要被完全删除的states (不包含 oldFocusState 和 new focus state)
              const filteredStates = this.filterOldState();
              //  获取当前需要展示的state列表
              // 新加入的 直接邻居 state ( new & old focus 都不包含)
              const newStates = Array.from(newVal.keys()).filter(
                (state) => state !== this.focusState
              );

              const originStates = this.showStateList;
              const showStateList = [
                ...new Set(
                  originStates
                    .filter((item) => !filteredStates.includes(item))
                    .concat(newStates)
                ),
              ];

              // 更新全局state 信息
              this.showStateList = showStateList;
              this.newStateList = newStates;
              // 更新重绑定数据，顶层DOM元素（svg 和 svgLinks）
              const [newSvgData, newLinkData] = this.updateGlobalDom(
                showStateList,
                newStates,
                filteredStates,
                false
              );
              this.svgLinkDatas = newLinkData;

              // 更新旧的focus state内的点
              this.updateOldFocusState(this.oldFocusState, false);
              // 画新加入的svg图
              this.addNewState(
                newStates.filter(
                  (state) =>
                    state !== this.focusState && state !== this.oldFocusState
                )
              );

              // 更新新focus图内的点 (checkIndex的更新（空白），会导致新加入的，当前focus的直接邻居重画大小)
              this.updateNewFocusState(this.focusState, false);

              // 更新全局力导图
              this.updateGlobalForce(newSvgData, newLinkData);
              this.focusedStates.add(this.focusState);
            }
          }
        } else {
          this.focusedStates.add(this.focusState);
          // 获取当前需要展示的state 列表
          this.showStateList = Array.from(newVal.keys());
          this.newStateList = this.showStateList.filter(
            (state) => state !== this.focusState
          );
          // initilize
          // 更新最大node数
          let maxNodeNum = d3.max(
            Array.from(newVal.values()),
            (d) => d.nodes.length
          );
          maxNodeNum =
            maxNodeNum > this.maxNodeNum ? maxNodeNum : this.maxNodeNum;
          this.maxNodeNum = maxNodeNum;
          this.setTopScale(maxNodeNum);
          this.drawGlobalGraph(newVal);
        }
      },
    },
    filterNode(newVal, oldVal) {
      const state = newVal.state;
      const oldState = oldVal.state;
      const oldSelectedId = this.selectedIds.get(state);

      if (oldSelectedId !== newVal.id || state !== oldState) {
        // get id array of neighbour
        const neighborMap = this.neighborMaps.get(state);
        const neighborSet = neighborMap.get(newVal.id);
        if (oldSelectedId) {
          const oldNeighborSet = neighborMap.get(oldSelectedId);
          this.neighborHighligt(
            oldSelectedId,
            oldNeighborSet,
            "selected",
            false,
            state
          );
        }
        this.selectedIds.set(state, newVal.id);
        this.neighborHighligt(newVal.id, neighborSet, "selected", true, state);

        if (newVal.id) {
          if (newVal["insight-list"].length > 1) {
            if (this.hidePanelMode) {
              if (this.showMoreIcon) {
                this.showMoreIcon = false;

                this.$nextTick(() => {
                  setTimeout(() => {
                    this.showMoreIcon = true;
                  }, 150);
                });
              } else {
                this.showMoreIcon = true;
              }
            } else {
              if (this.showMorePanel) {
                this.showMorePanel = false;

                this.$nextTick(() => {
                  setTimeout(() => {
                    this.showMorePanel = true;
                  }, 150);
                });
              } else {
                this.showMorePanel = true;
              }
            }
          } else {
            this.showMorePanel = false;
            this.showMoreIcon = false;
          }
        } else {
          this.showMorePanel = false;
          this.showMoreIcon = false;
        }
      }
    },
    // selectedNodes: {
    //   deep: true,
    //   handler(newVal) {
    //
    //   },
    // },
    checkIndex: {
      handler(newVal, oldVal) {
        this.$store.dispatch("table/convertCheckSelection", {
          mode: "checked",
          data: newVal,
        });

        // global links
        const globalBundleData = [];
        const linkGTop = d3
          .select("#force-svg-container")
          .select("#total-svg")
          .select("g.link-group");

        // get node map (key: state)
        const relatedNodeIdMap = new Map();
        for (let showId of newVal.keys()) {
          const stateMap = this.stateLinksMap.get(showId);

          if (stateMap) {
            for (let [state, nodeIds] of stateMap.entries()) {
              const singleStateIds = relatedNodeIdMap.get(state);

              if (singleStateIds) {
                singleStateIds.push(...nodeIds);
              } else {
                const newNodeIds = [];
                newNodeIds.push(...nodeIds);

                relatedNodeIdMap.set(state, newNodeIds);
              }
              nodeIds.forEach((targetId) => {
                const stateLineData = linkGTop
                  .select(`line.${this.focusState}_${state}`)
                  .datum();

                globalBundleData.push({
                  source: this.nodeIdMaps.get(this.focusState).get(showId),
                  target: this.nodeIdMaps.get(state).get(targetId),
                  middle: stateLineData,
                });
              });
            }
          }
        }
        for (let [state, ids] of relatedNodeIdMap.entries()) {
          // 去掉重复元素
          const newIds = [...new Set(ids)];
          relatedNodeIdMap.set(state, newIds);
        }
        // 根据该state的本身设置的保存条件，再筛选一次
        for (let [state, ids] of relatedNodeIdMap.entries()) {
          const selectedData = this.selectedDatas.get(state);
          if (selectedData) {
            relatedNodeIdMap.set(
              state,
              ids.filter((id) => selectedData.nodes.includes(id))
            );
          }
        }

        // get new sub graph Data
        const filteredAllStateData =
          this.getFilterSubGraphData(relatedNodeIdMap);

        Array.from(filteredAllStateData.keys()).forEach((state) => {
          const svg = d3
            .select("#force-svg-container")
            .select("#total-svg")
            .select("g.node-group")
            .select(`.${state}-state`);

          const newData = filteredAllStateData.get(state);

          // redraw inner force graph
          this.restart(true, state, newData);
          // global force graph update
          this.updateSvgSize(svg, this.svgRScale, newData.nodes.length);
        });
        // update link distance of svg
        this.globalSimulation.force("link").distance((d) => {
          const nodeNumS = d.source.nodeNum;
          const nodeNumT = d.target.nodeNum;
          return (
            this.linkDistanceScale(nodeNumS) + this.linkDistanceScale(nodeNumT)
          );
        });
        // 保存当前的bundleData
        this.globalBundleData = globalBundleData;

        // update bundle line attr, 对于新旧focus之间的bundle，需要判断新focus中的点有没有被filter掉， restart函数也要进行 oldBundle的筛选
        this.updateGlobalBundle(this.filterBundleBySelection(globalBundleData));

        // change "old focus" state links
        const oldFocusStateLinksMap = new Map();
        Array.from(newVal.keys()).forEach((id) => {
          oldFocusStateLinksMap.set(id, this.stateLinksMap.get(id));
        });
        this.oldFoucsStateLinksMaps.set(this.focusState, oldFocusStateLinksMap);
      },
      deep: true,
    },
    hoverIndex: {
      handler(newVal) {
        this.$store.dispatch("table/convertCheckSelection", {
          mode: "hovered",
          data: newVal.id
            ? new Map().set(newVal.id, {
                col: newVal.col,
                row: newVal.row,
              })
            : null,
        });

        this.crossStatesHoveredNeighbor = this.stateLinksMap.get(newVal.id);
      },
      deep: true,
    },
    // links data + node id list
    selectedData(newVal) {
      if (newVal) {
        const state = this.focusState;
        const simulation = this.simulations.get(state);
        this.selectedDatas.set(state, newVal);

        if (simulation) {
          simulation.stop();
          this.restart(true, state, newVal);

          if (!this.firstUpdateFlag) {
            this.updateGlobalBundle(
              this.filterBundleBySelection(this.globalBundleData)
            );
          }
          this.firstUpdateFlag = false;
        } else {
          // draw force graph
          this.drawGraph(newVal);
        }
      }
    },

    selectedNode(newVal, oldVal) {
      this.filterNode = newVal;
      if (newVal.id !== oldVal.id) {
        if (newVal.id) {
          this.$store.dispatch("table/convertCheckSelection", {
            mode: "clicked",
            data: new Map().set(newVal.id, {
              col: newVal.col,
              row: newVal.row,
            }),
          });
        } else {
          this.$store.dispatch("table/convertCheckSelection", {
            mode: "clicked",
            data: null,
          });
        }
      }
    },

    /* -------------------------------------------------------------------------- */
    // default config
    /* -------------------------------------------------------------------------- */
  },
  methods: {
    handleExploredPath(state, nodeId, mode) {
      const exploredPaths = this.exploredPaths;
      if (!exploredPaths.has(state)) {
        exploredPaths.set(state, []);
      }
      const exploredPath = exploredPaths.get(state);
      if (mode) {
        exploredPath.push(nodeId);
      } else {
        exploredPaths.set(
          state,
          exploredPath.filter((id) => id !== nodeId)
        );
      }
    },
    resetTableHighlight() {
      const selectedNode = this.selectedNode;
      const tableData =
        this.$store.getters["tree/allTableInfo"][this.focusState];
      this.$store.dispatch("table/loadHeadData", tableData);

      this.$store.dispatch("table/convertCheckSelection", {
        mode: "clicked",
        data: selectedNode.id
          ? new Map().set(selectedNode.id, {
              col: selectedNode.col,
              row: selectedNode.row,
            })
          : null,
      });

      this.$store.dispatch("table/convertCheckSelection", {
        mode: "checked",
        data: this.checkIndex,
      });
    },
    getTreeInfo() {
      const that = this;

      const nodeIdMaps = this.nodeIdMaps;
      const checkIndexs = this.checkIndexs;
      const checkedAllStateData = new Map();
      let allNodes = [];
      let allLinks = [];
      // 获取node data + state 内部的link data
      for (const [state, checkInfo] of checkIndexs) {
        if (checkInfo.size > 0) {
          // 检查每个state 的 checkIndex、
          const nodeIdMap = nodeIdMaps.get(state);
          const nodes = [];

          for (const id of checkInfo.keys()) {
            const nodeData = nodeIdMap.get(id);
            nodes.push({ ...nodeData });
          }
          allNodes.push(...nodes);

          const nodeIds = nodes.map((nodeData) => nodeData.id);
          const linkMaps = this.linkStateMaps.get(state);
          const links = linkMaps
            .filter(
              (d) => nodeIds.includes(d.source) && nodeIds.includes(d.target)
            )
            .map((d) => ({ ...d }));
          allLinks.push(...links);

          checkedAllStateData.set(state, {
            nodes: nodes,
            links: links,
          });
        }
      }
      // table 更新信息
      const stateList = Array.from(checkedAllStateData.keys());
      this.$store.dispatch("tree/loadTableInfo", {
        stateList: stateList,
      });
      this.$store.dispatch("table/convertCheckSelection", {
        mode: "checked",
        data: null,
      });

      this.$store.dispatch("table/convertCheckSelection", {
        mode: "clicked",
        data: null,
      });
      this.$store.dispatch("table/loadHeadData", null);

      // 获取跨state 的link data
      const totalNodeIds = allNodes.map((nodeData) => nodeData.id);
      const crossStateLinks = this.globalBundleData
        .filter((d) => {
          return (
            totalNodeIds.includes(d.source.id) &&
            totalNodeIds.includes(d.target.id)
          );
        })
        .map((d) => ({
          source: d.source.id,
          target: d.target.id,
          type: "state",
        }));
      crossStateLinks.push(
        ...this.preservedBundleData
          .filter((d) => {
            return (
              totalNodeIds.includes(d.source.id) &&
              totalNodeIds.includes(d.target.id)
            );
          })
          .map((d) => ({
            source: d.source.id,
            target: d.target.id,
            type: "state",
          }))
      );

      // 生成路径
      const nodeIdMap = new Map();
      allNodes.forEach((node) => {
        nodeIdMap.set(node.id, node);
      });
      const tree = { name: "root" };
      const children = [];

      const exploredPaths = this.exploredPaths;
      let allSingleStateRootId = [];
      // 所用点的tree node map
      const treeNodeMap = new Map();
      for (const [state, idStack] of exploredPaths) {
        if (idStack.length > 0) {
          const neighborMap = this.neighborMaps.get(state);

          // 生成tree node，并计入到tree node map中
          idStack.forEach((id) => {
            treeNodeMap.set(id, {
              name: id,
              forceData: nodeIdMap.get(id),
            });
          });
          // 本 state的 rootlist
          const rootList = [];

          // 按照最终 idStack 的入栈顺序，添加 children 信息
          idStack.forEach((id, index) => {
            const treeNode = treeNodeMap.get(id);
            let isRoot = true;
            // 找 parent node，如果找到，加入children，并且判定不是treeNode
            for (let i = index - 1; i >= 0; i--) {
              const parentId = idStack[i];

              const neighbors = neighborMap.get(parentId);
              if (neighbors && neighbors.includes(id)) {
                const parentTreeNode = treeNodeMap.get(parentId);
                if ("children" in parentTreeNode) {
                  parentTreeNode.children.push(id);
                } else {
                  parentTreeNode.children = [id];
                }
                isRoot = false;
                break;
              }
            }
            if (isRoot) {
              rootList.push(id);
            }
          });

          // 遍历每个root tree node，组成树结构
          rootList.forEach((id) => {
            const treeNode = treeNodeMap.get(id);
            addChild(treeNode, treeNodeMap);
            //singleStateTrees.push(treeNode);
          });

          allSingleStateRootId.push(...rootList);
        }
      }
      // 跨 state 连接每个子树
      crossStateLinks.forEach((link) => {
        const sourceId = link.source;
        const targetId = link.target;
        const sourceNode = treeNodeMap.get(sourceId);
        const targetNode = treeNodeMap.get(targetId);
        if ("children" in sourceNode) {
          sourceNode.children.push(targetNode);
        } else {
          sourceNode.children = [targetNode];
        }
        // 维持最终的 root id list
        if (allSingleStateRootId.includes(targetId)) {
          allSingleStateRootId = allSingleStateRootId.filter(
            (id) => id !== targetId
          );
        }
      });

      // const stateStack = [
      //   ...this.pathStack.filter((d) => d.state).map((d) => d.state),
      // ];
      // if (this.oldFocusState) {
      //   stateStack.push(this.oldFocusState);
      // }
      // if (this.focusState) {
      //   stateStack.push(this.focusState);
      // }
      // 将最终的 root tree node 加入到 root节点的 children 中
      allSingleStateRootId.forEach((rootId) => {
        children.push(treeNodeMap.get(rootId));
      });

      // const addedNodes = new Set();

      // if (checkedAllStateData.has("S0")) {
      //   checkedAllStateData.get("S0").nodes.forEach((node) => {
      //     const id = node.id;

      //     const newChild = {
      //       name: id,
      //       forceData: node,
      //     };
      //     addChildren(newChild);
      //     children.push(newChild);
      //   });
      // }

      // // 把没有连接上的其他树一起挂在第一层上
      // stateStack.forEach((state) => {
      //   if (checkedAllStateData.has(state)) {
      //     const nodes = checkedAllStateData.get(state).nodes;
      //     nodes.forEach((node) => {
      //       if (!addedNodes.has(node.id)) {
      //         const newChild = {
      //           name: node.id,
      //           forceData: node,
      //         };
      //         addChildren(newChild);
      //         children.push(newChild);
      //       }
      //     });
      //   }
      // });
      if (children.length > 0) {
        tree.children = children;
      }

      allLinks.push(...crossStateLinks);

      this.$store.commit("tree/setForceData", {
        tree: tree,
        nodeIdMap: nodeIdMap,
        linkData: allLinks,
      });

      function addChild(treeNode, treeNodeMap) {
        if ("children" in treeNode) {
          const children = treeNode.children;
          const newChildren = [];
          children.forEach((childId) => {
            const childTreeNode = treeNodeMap.get(childId);
            newChildren.push(childTreeNode);
            addChild(childTreeNode, treeNodeMap);
          });
          treeNode.children = newChildren;
        }
      }
      // 废弃的
      function addChildren(treeNode) {
        const nodeId = treeNode.name;
        addedNodes.add(nodeId);

        const relatedLinks = crossStateLinks.filter((d) => d.source === nodeId);
        if (relatedLinks.length > 0) {
          const children = [];
          relatedLinks.forEach((link) => {
            const newChild = {
              name: link.target,
              forceData: nodeIdMap.get(link.target),
            };
            children.push(newChild);
            addChildren(newChild);
          });
          treeNode.children = children;
        }
      }
    },

    enterAmplifyMode(state, mode) {
      const that = this;

      const svgTop = d3.select("#force-svg-container").select("#total-svg");
      svgTop
        .transition()
        .duration(this.durationTime)
        .style("background-color", () => (mode ? "#fff" : "transparent"));

      svgTop
        .selectChildren("g.link-group,g.bundle-group")
        .attr("opacity", mode ? 1 : 0)
        .transition()
        .duration(this.durationTime)
        .attr("opacity", mode ? 0 : 1)
        .on("end", function () {
          d3.select(this).classed("not-show", mode);
        });
      svgTop
        .select("g.node-group")
        .selectChildren("svg")
        .each(function (d) {
          if (d.id !== state && d.nodeNum !== 0) {
            d3.select(this)
              .attr("opacity", mode ? 1 : 0)
              .transition()
              .duration(that.durationTime)
              .attr("opacity", mode ? 0 : 1)
              .on("end", function () {
                d3.select(this).classed("not-show", mode);
              });
          }
        });

      const svg = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .select("g.node-group")
        .select(`.${state}-state`);

      svg
        .selectChildren(".background-shape, text, use")
        .attr("opacity", mode ? 1 : 0)
        .transition()
        .duration(this.durationTime)
        .attr("opacity", mode ? 0 : 1)
        .on("end", function () {
          d3.select(this).classed("not-show", mode);
        });
      svgTop
        .select(".shrink-icon")
        .attr("opacity", mode ? 0 : 1)
        .transition()
        .duration(this.durationTime)
        .attr("opacity", mode ? 1 : 0)
        .on("end", function () {
          d3.select(this).classed("not-show", !mode);
        });
      if (mode) {
        this.simulationRestart(this.simulations.get(this.focusState));
        this.simulationRestart(this.globalSimulation);
      }
    },
    filterBundleBySelection(bundleData) {
      const focusSelectedIds = this.selectedDatas.get(this.focusState).nodes;

      return bundleData
        .filter((d) => {
          const targetState = d.target.state;
          const targetSelectedData = this.selectedDatas.get(targetState);
          if (targetSelectedData) {
            return targetSelectedData.nodes.includes(d.target.id);
          } else {
            return true;
          }
        })
        .concat(
          this.preservedBundleData.filter((d) => {
            return (
              d.source.state !== this.oldFocusState ||
              d.target.state !== this.focusState ||
              focusSelectedIds.includes(d.target.id)
            );
          })
        );
    },
    updatePreservedBundle() {
      // 先保存oldState的bundle进栈
      this.pathStack.push({
        state: this.oldFocusState,
        bundleData: this.preservedBundleData,
      });
      const newCheckedIds = Array.from(this.checkIndex.keys());

      return this.preservedBundleData
        .filter(
          (d) =>
            d.middle.source.id !== this.oldFocusState ||
            d.middle.target.id !== this.focusState ||
            newCheckedIds.includes(d.target.id)
        )
        .concat(this.globalBundleData);
    },
    addOldFocusCheckedData(state, originNodeIds) {
      const oldCheckedIds = Array.from(this.checkIndexs.get(state).keys());
      return [...new Set(originNodeIds.concat(oldCheckedIds))];
    },
    addSvgIcon(svg, iconType) {
      const that = this;

      switch (iconType) {
        case "amplify":
          svg
            .append("use")
            .attr("class", "focus-icon")
            .attr("href", "#defs-amplify")
            .attr("x", "1%")
            .attr("y", "1%")
            .attr("width", "6%")
            .attr("height", "6%")
            .style("color", "transparent")
            .attr("cursor", "pointer")
            .on("click", function () {
              that.amplifyMode = true;
              const state = d3.select(this.parentNode).datum().id;
              that.enterAmplifyMode(state, true);
            })
            .on("mouseover", function () {
              d3.select(this)
                .classed("hover-highlight", true)
                .style("color", "#8d93a7");
            })
            .on("mouseleave", function () {
              d3.select(this)
                .classed("hover-highlight", false)
                .style("color", "transparent");
            });
          break;
        case "focus":
          svg
            .append("use")
            .attr("class", "focus-icon")
            .attr("href", "#defs-focus")
            .attr("x", "1%")
            .attr("y", "1%")
            .attr("width", "8%")
            .attr("height", "8%")
            .style("color", "transparent")
            .attr("cursor", "pointer")
            .on("mouseover", function () {
              d3.select(this)
                .classed("hover-highlight", true)
                .style("color", "#8d93a7");
            })
            .on("mouseleave", function () {
              d3.select(this)
                .classed("hover-highlight", false)
                .style("color", "transparent");
            })
            .on("click", function () {
              that.backMode = false;

              // 更新 preservedBundleData
              that.preservedBundleData = that.updatePreservedBundle();
              // load new data
              const state = d3.select(this.parentNode).datum().id;
              that.oldFocusState = that.focusState;
              that.focusState = state;
              const oldFocusStateLinksMap = that.oldFoucsStateLinksMaps.get(
                that.oldFocusState
              );

              for (const [id, stateMap] of oldFocusStateLinksMap.entries()) {
                // 如果有stateMap，才记录
                if (stateMap) {
                  oldFocusStateLinksMap.set(id, stateMap.get(that.focusState));
                }
              }

              that.$store.dispatch("force/loadData", {
                state: state,
              });
            });
          break;
      }
    },
    updateSvgSize(svg, svgRScale, nodeNum) {
      const that = this;
      const newBoundaryR = svgRScale(nodeNum);
      const newViewBoxScale = this.svgViewBoxScale(nodeNum);
      const newWidth = newBoundaryR * 2;
      const newHeight = newWidth;
      const viewBoxSize = newBoundaryR * newViewBoxScale;

      // reset transform
      const zoom = this.zooms.get(svg.datum().id);
      if (zoom) {
        svg.call(zoom.transform, d3.zoomIdentity);
      }
      if (nodeNum === 0) {
        svg
          .attr("opacity", 1)
          .transition()
          .duration(this.durationTime)
          .attr("opacity", 0)
          .on("end", function () {
            svg
              .classed("not-show", true)
              .attr("width", newWidth)
              .attr("height", newHeight)
              .attr("viewBox", [0, 0, viewBoxSize, viewBoxSize]);
          });
      } else {
        if (svg.classed("not-show") && !this.amplifyMode) {
          svg
            .classed("not-show", false)
            .attr("opacity", 0)
            .transition()
            .duration(this.durationTime)
            .attr("opacity", 1)
            .on("end", function () {
              svg

                .transition()
                .duration(that.durationTime * 2)
                .attr("width", newWidth)
                .attr("height", newHeight)
                .attr("viewBox", [0, 0, viewBoxSize, viewBoxSize]);
            });
        } else {
          svg
            .transition()
            .duration(this.durationTime * 2)
            .attr("width", newWidth)
            .attr("height", newHeight)
            .attr("viewBox", [0, 0, viewBoxSize, viewBoxSize]);
        }
      }

      // width 和 height 是为了 globalTick
      svg.datum().width = newWidth;
      svg.datum().height = newHeight;
      svg.datum().nodeNum = nodeNum;
      svg.datum().viewBoxR = viewBoxSize;
      svg.datum().boundaryR = newBoundaryR;

      svg.select(".state-text").attr("font-size", (d) => {
        if (d.id == this.focusState) return d.viewBoxR / 14;
        else return d.viewBoxR / 12;
      });

      const boundaryRectTmp = svg.datum().boundaryRectTmp;
      if (!boundaryRectTmp) {
        svg.datum().boundaryRectTmp = [0, 0, viewBoxSize, viewBoxSize];
      } else {
        boundaryRectTmp[0] = 0;
        boundaryRectTmp[1] = 0;
        boundaryRectTmp[2] = viewBoxSize;
        boundaryRectTmp[3] = viewBoxSize;
      }
      if (this.simulations.has(svg.datum().id)) {
        this.updatePositionForce(this.simulations.get(svg.datum().id), [
          viewBoxSize / 2,
          viewBoxSize / 2,
        ]);
      }
    },
    updateGlobalForce(nodes, links) {
      const simulation = this.globalSimulation;
      simulation.nodes(nodes);
      simulation.force("link").links(links);
      simulation.alphaDecay(this.defaultBaseConfig.alphaDecay);
      simulation.alpha(this.defaultBaseConfig.alpha);
      simulation.restart();
    },
    updateGlobalDom(
      showStateList,
      newStates,
      oldStates,
      darkMode,
      oldNewFocusState
    ) {
      const nodeGTop = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .select("g.node-group");
      const linkGTop = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .select("g.link-group");
      const svgNodeDatas = this.svgNodeDatas;
      const svgLinkDatas = this.svgLinkDatas;

      // 生成新的全局 svg data 和 link data
      const newSvgData = showStateList.map((state) => {
        if (svgNodeDatas.has(state)) {
          return svgNodeDatas.get(state);
        } else {
          const newData = {
            nodeNum: 0,
            id: state,
          };
          svgNodeDatas.set(state, newData);
          return newData;
        }
      });

      // 原来的linkData，去掉筛去的state
      const newLinkData1 = svgLinkDatas
        .filter(
          (d) =>
            !oldStates.includes(d.source.id) && !oldStates.includes(d.target.id)
        )
        .map((d) => ({
          source: d.source.id,
          target: d.target.id,
        }));

      // 新的link
      const newLinkData2 = newStates.map((state) => ({
        source: this.focusState,
        target: state,
      }));

      const newLinkData = newLinkData1.concat(newLinkData2);

      // update sub-svg dom element
      nodeGTop
        .selectChildren("svg")
        .data(newSvgData, (d) => d.id)
        .join(
          (enter) => {
            enter
              .append("svg")
              .attr("class", (d) => `${d.id}-state`)
              .attr("preserveAspectRatio", "xMinYMin meet")
              .call(this.globalDragDefine);
          },
          (update) => {
            if (!darkMode) {
              update
                .filter(
                  (d) => d.id !== this.oldFocusState && d.id !== this.focusState
                )
                .select("use.focus-icon")
                .classed("not-show", true);
            } else {
              update
                .filter(
                  (d) =>
                    this.newStateList.includes(d.id) ||
                    d.id === oldNewFocusState
                )
                .select("use.focus-icon")
                .classed("not-show", false);
            }
          },
          (exit) => {
            exit
              .attr("opacity", 1)
              .transition()
              .duration(this.durationTime)
              .attr("opacity", 0)
              .remove();
          }
        );
      linkGTop
        .selectChildren("line")
        .data(newLinkData, (d) => `${d.source}_${d.target}`)
        .join(
          (enter) => {
            enter
              .append("line")
              .attr("class", (d) => {
                return `${d.source}_${d.target}`;
              })
              // .attr("stroke", "#000");
              .attr("stroke", "none");
          },
          (update) => update,
          (exit) => {
            exit
              .attr("opacity", 1)
              .transition()
              .duration(this.durationTime)
              .attr("opacity", 0)
              .remove();
          }
        );
      return [newSvgData, newLinkData];
    },
    addNewState(newStates) {
      newStates.forEach((state) => {
        this.drawSubGraph({
          state: state,
          data: {
            nodes: this.nodeStateMaps.get(state).map((d) => d.id),
            links: this.linkStateMaps.get(state),
          },
        });
      });
    },
    getSvgInnterSizeScale(nodes) {
      let maxVegaLiteNum = 0;
      nodes.forEach((node) => {
        const vegaLiteNum = node["insight-list"].length;
        if (vegaLiteNum > maxVegaLiteNum) maxVegaLiteNum = vegaLiteNum;
      });

      const circleRScale = d3
        .scaleLog([1, maxVegaLiteNum], [this.circleR, this.circleR * 2])
        .base(2);
      const insightSizeScale = d3
        .scaleLog(
          [1, maxVegaLiteNum],
          [this.insightIconSize, this.insightIconSize * 2]
        )
        .base(2);
      return [circleRScale, insightSizeScale];
    },
    updateNewFocusState(state, backMode) {
      const that = this;
      const nodeData = this.nodeStateMaps.get(state);
      const linkData = this.linkStateMaps.get(state);
      const svg = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .select("g.node-group")
        .select(`.${state}-state`)
        .classed("focus-svg", true);

      // 重设focus svg的宽和高
      this.updateSvgSize(svg, this.svgRScale, nodeData.length);
      svg.datum().pinned = true;
      svg.datum().fx = this.containerWidth / 2;
      svg.datum().fy = this.containerHeight / 2;

      svg
        .select("use.focus-icon")
        .attr("href", "#defs-amplify")
        .attr("width", "6%")
        .attr("height", "6%")
        .on("click", function () {
          const state = d3.select(this.parentNode).datum().id;
          that.amplifyMode = true;
          that.enterAmplifyMode(state, true);
        })
        .on("mouseover", function () {
          d3.select(this)
            .classed("hover-highlight", true)
            .style("color", "#8d93a7");
        })
        .on("mouseleave", function () {
          d3.select(this)
            .classed("hover-highlight", false)
            .style("color", "transparent");
        });

      // 更新nodeIdMap (如果需要的话)
      if (!backMode && !this.focusedStates.has(state)) {
        const nodeIdMap = this.nodeIdMaps.get(state);
        const originNodeIdMap = new Map();

        const oldNodeIds = Array.from(nodeIdMap.keys());
        const [circleRScale, insightSizeScale] =
          this.getSvgInnterSizeScale(nodeData);
        this.circleRScales.set(state, circleRScale);
        this.insightSizeScales.set(state, insightSizeScale);

        nodeData.forEach((d) => {
          originNodeIdMap.set(d.id, d);
          if (!oldNodeIds.includes(d.id)) {
            const insightNum = d["insight-list"].length;
            nodeIdMap.set(d.id, {
              ...d,
              insightIndex: 0,
              insightIndexList: [...Array(insightNum).keys()],
              circleR: circleRScale(insightNum),
              iconSize: insightSizeScale(insightNum),
              showDetail: false,
              pinned: false,
              checked: false,
              view: null,
              img: null,
              rect: null,
            });
          }
        });
        this.originNodeIdMaps.set(state, originNodeIdMap);
      }
      this.$store.dispatch("force/setStatisticGraph", {
        state: state,
        data: {
          nodes: nodeData,
          links: linkData,
        },
      });

      // 更新辅助数据结构
      this.showIndex = this.showIndexs.get(state);
      this.pinnedIndex = this.pinnedIndexs.get(state);
      this.hoverIndex = this.hoverIndexs.get(state);
      this.selectedNode = this.selectedNodes.get(state);
      this.checkIndex = this.checkIndexs.get(state);
    },

    updateOldFocusState(state, backMode) {
      const that = this;
      const oldFocusSvg = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .select("g.node-group")
        .select(".focus-svg")
        .classed("focus-svg", false);

      if (backMode) {
        oldFocusSvg
          .select("use.focus-icon")
          .attr("href", "#defs-focus")
          .attr("width", "8%")
          .attr("height", "8%")
          .style("color", "transparent")
          .on("mouseover", function () {
            d3.select(this)
              .classed("hover-highlight", true)
              .style("color", "#8d93a7");
          })
          .on("mouseleave", function () {
            d3.select(this)
              .classed("hover-highlight", false)
              .style("color", "transparent");
          })
          .on("click", function () {
            that.backMode = false;
            // 更新 preservedBundleData
            that.preservedBundleData = that.updatePreservedBundle();
            // load new data
            const state = d3.select(this.parentNode).datum().id;

            that.oldFocusState = that.focusState;
            that.focusState = state;

            const oldFocusStateLinksMap = that.oldFoucsStateLinksMaps.get(
              that.oldFocusState
            );

            for (const [id, stateMap] of oldFocusStateLinksMap.entries()) {
              // 如果有stateMap，才记录
              if (stateMap) {
                oldFocusStateLinksMap.set(id, stateMap.get(that.focusState));
              }
            }

            that.$store.dispatch("force/loadData", {
              state: state,
            });
          });
      } else {
        // 获取需要保存的nodes和links数据
        const preservedNodeIds = Array.from(this.checkIndex.keys());

        const linkData = this.selectedDatas.get(state).links;
        const preservedLinks = linkData.filter(
          (d) =>
            preservedNodeIds.includes(d.source) &&
            preservedNodeIds.includes(d.target)
        );

        this.restart(true, state, {
          links: preservedLinks,
          nodes: preservedNodeIds,
        });
        this.updateSvgSize(
          oldFocusSvg,
          this.svgRScale,
          preservedNodeIds.length
        );
        oldFocusSvg
          .select("use.focus-icon")
          .attr("href", "#defs-back")
          .style("color", "transparent")
          .on("click", function () {
            that.backMode = true;
            // load new data
            const state = d3.select(this.parentNode).datum().id;
            that.oldFocusState = that.focusState;
            that.focusState = state;

            that.$store.dispatch("force/loadData", {
              state: state,
            });
          });
      }

      // change data in sub-svg
      oldFocusSvg.datum().fx = null;
      oldFocusSvg.datum().fy = null;
      oldFocusSvg.datum().pinned = false;
    },
    filterOldState() {
      const that = this;
      const svgTop = d3.select("#force-svg-container").select("#total-svg");
      // 获取需要删除的子svg和id列表
      const filteredSvgs = svgTop
        .select("g.node-group")
        .selectChildren("svg")
        .filter(
          (d) =>
            d.nodeNum === 0 &&
            d.id !== this.oldFocusState &&
            d.id !== this.focusState
        );
      const filteredIds = [];
      filteredSvgs.each((d) => filteredIds.push(d.id));

      return filteredIds;
    },
    updateGlobalBundle(globalBundleData) {
      const bundleG = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .select("g.bundle-group");
      bundleG
        .selectAll("path")
        .data(globalBundleData, (d) => {
          return `${d.source.id}-${d.target.id}`;
        })
        .join(
          (enter) => {
            enter
              .append("path")
              .attr("fill", "none")
              .attr("stroke", "#858eb5")
              .attr("stroke-opacity", "0.3")
              .attr("opacity", 0)
              .transition()
              .duration(this.durationTime)
              .attr("opacity", 1);
          },
          (update) => {
            update.transition().duration(this.durationTime);
          },
          (exit) => {
            exit
              .attr("opacity", 1)
              .transition()
              .duration(this.durationTime)
              .attr("opacity", 0)
              .remove();
          }
        );
    },

    getFilterSubGraphData(relatedNodeIdMap) {
      const newStateList = this.newStateList;
      const filteredNodeData = new Map();
      for (const [state, nodeIds] of relatedNodeIdMap) {
        const oldNodeData = filteredNodeData.get(state);
        if (oldNodeData) {
          oldNodeData.push(...nodeIds);
        } else {
          filteredNodeData.set(state, nodeIds);
        }
      }

      const filteredLinkData = new Map();
      for (const [state, nodeIds] of relatedNodeIdMap) {
        let linkData = this.linkStateMaps.get(state);
        if (this.selectedDatas.get(state)) {
          linkData = this.selectedDatas.get(state).links;
        }

        filteredLinkData.set(
          state,
          Array.from(linkData.values()).filter(
            (d) => nodeIds.includes(d.source) && nodeIds.includes(d.target)
          )
        );
      }

      const allStatesData = new Map();
      newStateList.forEach((state) => {
        // 只对当前新增的直接邻居做改变

        const nodes = filteredNodeData.get(state);
        if (nodes) {
          allStatesData.set(state, {
            links: filteredLinkData.get(state),
            nodes: filteredNodeData.get(state),
          });
        } else {
          allStatesData.set(state, {
            links: [],
            nodes: [],
          });
        }
      });
      return allStatesData;
    },

    domUpdate(nodes, links, nodeSingleG, linkSingleG, state) {
      const that = this;
      const showIndex = this.showIndexs.get(state);
      const pinnedIndex = this.pinnedIndexs.get(state);
      const checkIndex = this.checkIndexs.get(state);
      const simulation = this.simulations.get(state);

      // rebind data of dom elements
      let nodeG = null;
      let linkG = null;
      linkSingleG
        .selectAll("g")
        .data(links, (d) => {
          if (typeof d.source === "object") {
            return `${d.source.id}_${d.target.id}`;
          } else {
            return `${d.source}_${d.target}`;
          }
        })
        .join(
          (enter) => {
            linkG = enter.append("g");
            return linkG;
          },
          (update) => update,
          (exit) => {
            exit
              .attr("opacity", 1)
              .transition()
              .duration(this.durationTime)
              .attr("opacity", 0)
              .remove();
          }
        );

      nodeSingleG
        .selectChildren("g")
        .data(nodes, (d) => d.id)
        .join(
          (enter) => {
            nodeG = enter.append("g");
          },
          (update) => {
            // update all vega-lite graph
            update.each(function (d) {
              const g = d3.select(this);
              const id = d.id;
              const view = showIndex.get(id);
              if (view) {
                view.finalize();
                g.selectAll(".vega-lite-graph").remove();
                g.datum().view = null;
                g.datum().img = null;
                that.drawVegaLite(
                  g,
                  pinnedIndex.get(id) ? "svg" : "img",
                  state
                );
              }
            });

            // update circle attr
            update
              .select(".circle")
              .attr("r", function () {
                return d3.select(this.parentNode).datum().circleR;
              })
              .attr("fill", function () {
                const gData = d3.select(this.parentNode).datum();
                return that.nodeTypeColor(
                  gData["insight-list"][gData.insightIndex]["insight-category"]
                );
              });
            // update icon
            update
              .select(".insight-icon")
              .attr("href", function () {
                return that.setInsightIcon(this);
              })
              .attr("class", "insight-icon")
              .attr("width", function () {
                return d3.select(this.parentNode).datum().iconSize;
              })
              .attr("height", function () {
                return d3.select(this.parentNode).datum().iconSize;
              })
              .attr("x", function () {
                return -d3.select(this.parentNode).datum().iconSize / 2;
              })
              .attr("y", function () {
                return -d3.select(this.parentNode).datum().iconSize / 2;
              });
          },
          (exit) => {
            exit
              .each((data) => {
                const id = data.id;

                if (pinnedIndex.has(id)) {
                  pinnedIndex.delete(id);
                  data.fx = null;
                  data.fy = null;
                }
                if (showIndex.has(id)) {
                  showIndex.delete(id);
                }
                if (checkIndex.has(id)) {
                  checkIndex.delete(id);
                  this.handleExploredPath(state, id, false);
                }

                data.showDetail = false;
                data.pinned = false;
                data.checked = false;
                data.view = null;
                data.img = null;
                data.rect = null;
              })
              .attr("opacity", 1)
              .transition()
              .duration(this.durationTime)
              .attr("opacity", 0)
              .remove();
          }
        );

      this.setDomAttributes(linkG, nodeG, state);

      // rebind data of simulation
      simulation.nodes(nodes);
      simulation.force("link").links(links);

      // reset alpha to reheat
      this.simulationRestart(simulation);
    },
    simulationRestart(simulation) {
      simulation.alphaDecay(this.defaultBaseConfig.alphaDecay);
      simulation.alpha(this.defaultBaseConfig.alpha);
      simulation.restart();
    },
    setTopScale(maxNodeNum) {
      const svgContainer = d3.select("#force-svg-container");
      this.containerWidth = parseInt(svgContainer.style("width"), 10);
      this.containerHeight = parseInt(svgContainer.style("height"), 10);
      const maxR =
        (this.containerWidth > this.containerHeight
          ? this.containerHeight
          : this.containerWidth) / 2.5;

      this.svgRScale = d3.scaleLinear([0, maxNodeNum], [100, maxR]);
      this.linkDistanceScale = d3.scaleLinear(
        [0, maxNodeNum],
        [150, maxR * 1.5]
      );
      this.chargeStrengthScale = d3.scaleLinear(
        [0, maxNodeNum],
        [-2000, -5000]
      );
      this.svgViewBoxScale = d3.scaleLinear([0, maxNodeNum], [2, 4]);
    },
    hideMoreBox() {
      this.hidePanelMode = true;
      this.showMorePanel = false;
      this.showMoreIcon = true;
    },
    setInsightIcon(that) {
      const gData = d3.select(that.parentNode).datum();
      const group = gData["insight-list"][gData.insightIndex]["insight-type"];

      let insightType = null;
      switch (group) {
        case "dominance":
          insightType = "dominance";
          break;
        case "outlier":
          insightType = "outlier";
          break;
        case "outlier-temporal":
          insightType = "outlier-temporal";
          break;
        case "top2":
          insightType = "top2";
          break;
        case "evenness":
          insightType = "evenness";
          break;
        case "trend":
          insightType = "trend";
          break;
        case "skewness":
          insightType = "skewness";
          break;
        case "kurtosis":
          insightType = "kurtosis";
          break;
        case "correlation":
        case "correlation-temporal":
          insightType = "correlation";
          break;
      }
      return "#defs-" + insightType;
    },
    changeInsightIndex(selectedIndex) {
      const that = this;
      const id = this.filterNode.id;
      const state = this.filterNode.state;
      const showIndex = this.showIndexs.get(state);
      const pinnedIndex = this.pinnedIndexs.get(state);

      // change index record of filterNode
      this.filterNode.insightIndex = selectedIndex;

      const nodeData = this.nodeIdMaps.get(state).get(id);
      // change data record in force graph
      nodeData.insightIndex = selectedIndex;

      const newType = nodeData["insight-list"][selectedIndex]["insight-type"];
      const g = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group")
        .select(`.${state}-state`)
        .select(".node-group")
        .selectChildren("g")
        .filter((d) => d.id === id);

      //change insight icon
      g.select(".insight-icon").attr("href", function () {
        return that.setInsightIcon(this);
      });
      // change vega-lite graph
      showIndex.get(id).finalize();

      g.select(".vega-lite-graph").remove();
      g.datum().view = null;
      g.datum().img = null;
      this.drawVegaLite(g, pinnedIndex.get(id) ? "svg" : "img", state);
    },

    setDomAttributes(linkG, circleG, state) {
      const that = this;

      const selectedNodes = this.selectedNodes;

      const simulation = this.simulations.get(state);
      const hoverIndex = this.hoverIndexs.get(state);
      const checkIndex = this.checkIndexs.get(state);
      const pinnedIndex = this.pinnedIndexs.get(state);
      const neighborMaps = this.neighborMaps;
      const showIndex = this.showIndexs.get(state);

      circleG
        .attr("opacity", 0)
        .transition()
        .duration(this.durationTime)
        .attr("opacity", 1);
      linkG
        .attr("opacity", 0)
        .transition()
        .duration(this.durationTime)
        .attr("opacity", 1);

      const nodeTypeColor = d3.scaleOrdinal(
        ["point", "shape", "compound"],

        ["#C69DE9", "#F7A69F", "#53C4B6"]
      );
      this.nodeTypeColor = nodeTypeColor;

      // 画links
      const linkGroup = linkG
        .append("line")
        .attr("class", "link")
        .attr("stroke", "#555")
        .attr("stroke-opacity", 0.6)
        .attr("class", "network-line")
        .attr("stroke-width", 1);

      const showIndexList = Array.from(showIndex.keys());

      linkGroup.each(function (d) {
        const sourceId = d.source;
        const targetId = d.target;
        if (typeof sourceId == "string") {
          if (
            showIndexList.includes(sourceId) ||
            showIndexList.includes(targetId)
          ) {
            const linkType = d.type;

            switch (linkType) {
              case "siblings":
                // 普通实线

                break;

              case "parent-child":
                // 锥形线
                d3.select(this).classed("not-show", true);
                d3.select(this.parentNode)
                  .append("path")
                  .attr("class", "network-angle")
                  .attr("fill", "#ccc");
                break;
              case "same-name":
                // s-a: 虚线
                d3.select(this).style("stroke-dasharray", "10,5");
                break;
            }
          }
        }
      });

      //画nodes
      const circleGroup = circleG
        .append("circle")
        .attr("class", "circle normal-circle")
        .classed("not-show", function () {
          const gData = d3.select(this.parentNode).datum();
          return gData.showDetail;
        })
        .attr("r", function () {
          return d3.select(this.parentNode).datum().circleR;
        })
        .attr("fill", function () {
          const gData = d3.select(this.parentNode).datum();
          return nodeTypeColor(
            gData["insight-list"][gData.insightIndex]["insight-category"]
          );
        })
        .style("transition", "transform 0.2s")
        .on("mouseover", function () {
          circleMouseover(that, this, hoverIndex);
        })
        .on("mouseout", function () {
          circleMouseout(that, this, hoverIndex);
        })
        .on("click", function () {
          circleClick(
            that,
            this,
            simulation,
            changeLinkStyle,
            togglePin,
            nodeTypeColor
          );
        });

      const containerGroup = circleG;

      const iconGroup = containerGroup
        .append("use")
        .attr("href", function () {
          return that.setInsightIcon(this);
        })
        .attr("class", "insight-icon")
        .attr("width", function () {
          return d3.select(this.parentNode).datum().iconSize;
        })
        .attr("height", function () {
          return d3.select(this.parentNode).datum().iconSize;
        })
        .attr("x", function () {
          return -d3.select(this.parentNode).datum().iconSize / 2;
        })
        .attr("y", function () {
          return -d3.select(this.parentNode).datum().iconSize / 2;
        })
        .attr("pointer-events", "none")
        .style("transition", "transform 0.2s");

      const rectGroup = containerGroup
        .append("rect")
        .attr("class", "rect vega-lite-border")
        .classed("not-show", function () {
          const gData = d3.select(this.parentNode).datum();
          return !gData.showDetail;
        })
        .attr("fill", "#fff")
        .attr("stroke", "#ccc")
        .attr("stroke-width", 1.5)
        .attr("cursor", "pointer")
        .on("mouseover", function () {
          rectMouseover(that, this, neighborMaps, hoverIndex);
        })
        .on("mouseout", function () {
          rectMouseout(that, this, neighborMaps, hoverIndex);
        })
        .on("click", function () {
          rectClick(that, this);
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

      const svg = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group")
        .select(`.${state}-state`);

      const dragDefine = d3
        .drag()
        .container(function () {
          // 选择顶层nodeGy元素作为容器，影响 event.x和event.y
          return svg.selectChild(".node-group").node();
        })
        .subject(function (event) {
          // 将父元素 g 作为 subject 返回 (因为数据挂载在父元素g上)
          return d3.select(this.parentNode).datum();
        })
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
      // 设置结点拖动行为，也是只在圆上设置，避免与vega-lite图的鼠标事件冲突
      svg
        .selectChild(".node-group")
        .selectChildren("g")
        .selectChild(".circle")
        .call(dragDefine);
      svg
        .selectChild(".node-group")
        .selectChildren("g")
        .selectChild(".rect")
        .call(dragDefine);

      function circleMouseover(self, that, hoverIndex) {
        const d = d3.select(that.parentNode).datum();
        const id = d.id;
        Object.assign(hoverIndex, {
          id: id,
          col: d.col,
          row: d.row,
        });

        if (!d.showDetail) {
          d3.select(that)
            .attr("fill", function () {
              return d3.color(d3.select(that).attr("fill")).brighter(0.4);
            })
            .style("cursor", "pointer")
            .attr("transform", "scale(2)");

          d3.select(that.parentNode)
            .select(".insight-icon")
            .attr("transform", "scale(2)");
        }

        if (state === self.oldFocusState) {
          const oldFocusStateLinksMap = self.oldFoucsStateLinksMaps.get(state);

          self.crossStatesNeighborHighlight(
            oldFocusStateLinksMap.get(id),
            true,
            self.focusState
          );
        }
        if (self.newStateList.includes(state) || state === self.oldFocusState) {
          self.$store.dispatch("table/convertCrossStateHoverSelection", {
            data: {
              id: d.id,
              col: d.col,
              row: d.row,
            },
          });
        }
      }
      function circleMouseout(self, that, hoverIndex) {
        const d = d3.select(that.parentNode).datum();
        const id = d.id;
        // hoverIndex.id = null;
        // hoverIndex.col = null;
        // hoverIndex.row = null;
        Object.assign(hoverIndex, {
          id: null,
          col: null,
          row: null,
        });
        if (!d.showDetail) {
          d3.select(that)
            .attr("transform", "scale(1)")
            .attr("fill", function () {
              const gData = d3.select(that.parentNode).datum();

              return nodeTypeColor(
                gData["insight-list"][gData.insightIndex]["insight-category"]
              );
            });
        }
        d3.select(that.parentNode)
          .select(".insight-icon")
          .attr("transform", "scale(1)");

        if (state === self.oldFocusState) {
          const oldFocusStateLinksMap = self.oldFoucsStateLinksMaps.get(state);

          self.crossStatesNeighborHighlight(
            oldFocusStateLinksMap.get(id),
            false,
            self.focusState
          );
        }
        if (self.newStateList.includes(state) || state === self.oldFocusState) {
          self.$store.dispatch("table/convertCrossStateHoverSelection", {
            data: null,
          });
        }
      }
      function togglePin() {
        const g = d3.select(this.parentNode);
        const pinned = !g.datum().pinned;
        g.datum().pinned = pinned;
        g.classed("pinned", true);
        if (pinned) {
          g.datum().fx = g.datum().x;
          g.datum().fy = g.datum().y;
          g.select(".pin").classed("icon-pinned", true);

          that.drawVegaLite(g, "svg", state);
          pinnedIndex.set(g.datum().id, g);
        } else {
          g.classed("pinned", false);
          g.select(".pin").classed("icon-pinned", false);
          g.datum().fx = null;
          g.datum().fy = null;
          that.drawVegaLite(g, "img", state);
          pinnedIndex.delete(g.datum().id);
        }
      }
      function changeLinkStyle(nodeId, showMode) {
        // change style of links
        const linkG = d3
          .select("#force-svg-container")
          .select("svg")
          .select("g.node-group")
          .select(`svg.${state}-state`)
          .select("g.link-group");

        // 选择出作为邻居的link-g元素
        const neighborLinkG = linkG.selectChildren("*").filter((d) => {
          return d.source.id == nodeId || d.target.id == nodeId;
        });
        neighborLinkG.selectChildren("line.network-line").each(function (d, i) {
          const linkType = d.type;

          if (showMode) {
            switch (linkType) {
              case "siblings":
                // 普通实线

                break;

              case "parent-child":
                // 锥形线
                d3.select(this).classed("not-show", true);
                d3.select(this.parentNode)
                  .append("path")
                  .attr("class", "network-angle")
                  .attr("fill", "#ccc");
                break;
              case "same-name":
                // s-a: 虚线
                d3.select(this).style("stroke-dasharray", "10,5");
                break;
            }
          } else {
            switch (linkType) {
              case "siblings":
                // 普通实线

                break;
              case "state":
                break;
              case "parent-child":
                // 锥形线
                d3.select(this).classed("not-show", false);
                d3.select(this.parentNode)
                  .select("path.network-angle")
                  .remove();

                break;
              case "same-name":
                // s-a: 虚线
                d3.select(this).style("stroke-dasharray", "none");
                break;
            }
          }
        });
      }

      function circleClick(
        self,
        that,
        simulation,
        changeLinkStyle,
        togglePin,
        nodeTypeColor
      ) {
        // ! 注意selectedNode,只能通过self访问，watch才能及时响应
        // 获取选择circle对应的container - g元素
        const g = d3.select(that.parentNode);

        // selectedNode 记录
        if (state === self.focusState) {
          self.selectedNode = {
            id: g.datum().id,
            state: state,
            insightIndex: g.datum().insightIndex,
            "insight-list": g.datum()["insight-list"],
            col: g.datum().col,
            row: g.datum().row,
          };
          selectedNodes.set(state, self.selectedNode);
        } else {
          selectedNodes.set(state, {
            id: g.datum().id,
            state: state,
            insightIndex: g.datum().insightIndex,
            "insight-list": g.datum()["insight-list"],
            col: g.datum().col,
            row: g.datum().row,
          });
          self.filterNode = {
            id: g.datum().id,
            state: state,
            insightIndex: g.datum().insightIndex,
            "insight-list": g.datum()["insight-list"],
          };
        }

        // 显示vega-lite图
        if (!g.datum().showDetail) {
          g.datum().showDetail = true;

          const circle = d3.select(that);
          const rect = g.selectChild(".rect");
          const insightIcon = g.selectChild(".insight-icon");
          const rectTitle = g.select(".rect-title");
          const rectText = g.selectChildren(".title-text");

          rect.classed("not-show", false);
          rectTitle.classed("not-show", false);
          rectText.classed("not-show", false);
          circle.classed("not-show", true);
          insightIcon.classed("not-show", true);

          g.append("use")
            .attr("href", "#defs-remove")
            .attr("class", "remove vega-lite-icon")
            .attr("cursor", "pointer")
            .on("click", function () {
              g.datum().showDetail = false;
              g.datum().pinned = false;

              g.classed("pinned", false);
              g.datum().fx = null;
              g.datum().fy = null;
              if (state === self.focusState) {
                self.selectedNode = {
                  id: null,
                  state: state,
                  insightIndex: null,
                  "insight-list": null,
                  col: null,
                  row: null,
                };
                selectedNodes.set(state, self.selectedNode);
              } else {
                selectedNodes.set(state, {
                  id: null,
                  state: state,
                  insightIndex: null,
                  "insight-list": null,
                  col: null,
                  row: null,
                });
                self.filterNode = {
                  id: null,
                  state: state,
                  insightIndex: null,
                  "insight-list": null,
                };
              }

              g.selectChildren(".vega-lite-icon").remove();
              self.deleteVegaLite(g, state);
              const collideForce = simulation.force("collide");
              const bodyForce = simulation.force("charge");
              const linkForce = simulation.force("link");
              if (collideForce)
                collideForce.initialize(simulation.nodes(), d3.randomLcg);
              if (linkForce)
                linkForce.initialize(simulation.nodes(), d3.randomLcg);
              if (bodyForce) {
                simulation.force("charge", null);
                simulation.force("charge", bodyForce);
              }
              rect.classed("not-show", true);
              rectTitle.classed("not-show", true);
              rectText.classed("not-show", true);
              circle
                .classed("not-show", false)
                .attr("transform", "scale(1)")
                .attr("fill", function () {
                  const gData = d3.select(that.parentNode).datum();

                  return nodeTypeColor(
                    gData["insight-list"][gData.insightIndex][
                      "insight-category"
                    ]
                  );
                });

              insightIcon.classed("not-show", false);
              changeLinkStyle(g.datum().id, false);
              self.simulationRestart(simulation);
            });

          g.append("use")
            .attr("href", "#defs-pin")
            .attr("class", "pin vega-lite-icon")
            .attr("cursor", "pointer")
            .on("click", togglePin);

          g.append("use")
            .attr("href", "#defs-check")
            .attr("class", "check vega-lite-icon")
            .attr("cursor", "pointer")
            .on("click", function () {
              toggleCheck(self, this, checkIndex);
            });

          self.drawVegaLite(g, "img", state);

          const nodeId = g.datum().id;
          changeLinkStyle(nodeId, true);
        }
      }

      function rectMouseover(self, that, neighborMaps, hoverIndex) {
        //颜色变，表示被选中
        const neighborMap = neighborMaps.get(state);
        const rect = d3.select(that);
        const parentNode = d3.select(that.parentNode);
        const d = d3.select(that.parentNode).datum();
        const id = parentNode.datum().id;
        const neighbor = neighborMap.get(id);
        self.neighborHighligt(id, neighbor, "hover", true, state);
        rect.classed("center-highlight", true);
        parentNode.select(".rect-title").classed("center-highlight", true);

        Object.assign(hoverIndex, {
          id: id,
          col: parentNode.datum().col,
          row: parentNode.datum().row,
        });

        // old focus 的hover高亮 new focus
        if (state === self.oldFocusState) {
          const oldFocusStateLinksMap = self.oldFoucsStateLinksMaps.get(state);

          self.crossStatesNeighborHighlight(
            oldFocusStateLinksMap.get(id),
            true,
            self.focusState
          );
        }
        if (self.newStateList.includes(state) || state === self.oldFocusState) {
          self.$store.dispatch("table/convertCrossStateHoverSelection", {
            data: {
              id: d.id,
              col: d.col,
              row: d.row,
            },
          });
        }
      }
      function rectMouseout(self, that, neighborMaps, hoverIndex) {
        const neighborMap = neighborMaps.get(state);
        const rect = d3.select(that);
        const parentNode = d3.select(that.parentNode);
        const id = parentNode.datum().id;
        const neighbor = neighborMap.get(id);
        self.neighborHighligt(id, neighbor, "hover", false, state);
        Object.assign(hoverIndex, {
          id: null,
          col: null,
          row: null,
        });
        if (id !== selectedNodes.get(state).id) {
          rect.classed("center-highlight", false);
          parentNode.select(".rect-title").classed("center-highlight", false);
        }

        if (state === self.oldFocusState) {
          const oldFocusStateLinksMap = self.oldFoucsStateLinksMaps.get(state);

          self.crossStatesNeighborHighlight(
            oldFocusStateLinksMap.get(id),
            false,
            self.focusState
          );
        }
        if (self.newStateList.includes(state) || state === self.oldFocusState) {
          self.$store.dispatch("table/convertCrossStateHoverSelection", {
            data: null,
          });
        }
      }
      function rectClick(self, that) {
        // ! 注意:selectedNode
        // 获取对应的container - g元素
        const g = d3.select(that.parentNode);
        if (state === self.focusState) {
          self.selectedNode = {
            id: g.datum().id,
            state: state,
            insightIndex: g.datum().insightIndex,
            "insight-list": g.datum()["insight-list"],
            col: g.datum().col,
            row: g.datum().row,
          };
          selectedNodes.set(state, self.selectedNode);
        } else {
          selectedNodes.set(state, {
            id: g.datum().id,
            state: state,
            insightIndex: g.datum().insightIndex,
            "insight-list": g.datum()["insight-list"],
            row: g.datum().row,
            col: g.datum().col,
          });
          self.filterNode = {
            id: g.datum().id,
            state: state,
            insightIndex: g.datum().insightIndex,
            "insight-list": g.datum()["insight-list"],
          };
        }
      }
      // 拖动开始时，重新加热迭代过程，并且修正被拖动点的fx,fy
      function dragstarted(event) {
        if (!event.active) {
          simulation
            .alphaTarget(
              +that.defaultBaseConfig.alphaTarget + 0.3 > 1
                ? 1
                : +that.defaultBaseConfig.alphaTarget + 0.3
            )
            .restart();
        }

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
        if (!event.active) {
          simulation.alphaTarget(that.defaultBaseConfig.alphaTarget);
        }

        if (event.subject.pinned) {
          event.subject.fx = event.subject.x;
          event.subject.fy = event.subject.y;
        } else {
          event.subject.fx = null;
          event.subject.fy = null;
        }
      }

      function toggleCheck(self, that, checkIndex) {
        //  只能focus状态togglecheck
        if (state === self.focusState) {
          const g = d3.select(that.parentNode);
          const checked = !g.datum().checked;
          g.datum().checked = checked;
          if (checked) {
            checkIndex.set(g.datum().id, {
              row: g.datum().row,
              col: g.datum().col,
            });

            g.select(".check").classed("icon-pinned", true);
            g.selectChildren("rect, circle").classed("svg-inset", true);
            self.handleExploredPath(state, g.datum().id, true);
          } else {
            checkIndex.delete(g.datum().id);
            g.select(".check").classed("icon-pinned", false);
            g.selectChildren("rect,circle").classed("svg-inset", false);
            self.handleExploredPath(state, g.datum().id, false);
          }
        }
      }
    },

    neighborHighligt(id, neighbor, type, enable, state) {
      const className = type + "-highlight";
      const nodeGroup = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group")
        .select(`.${state}-state`)
        .select(".node-group")
        .selectChildren("g");

      const linkGroup = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group")
        .select(`.${state}-state`)
        .select(".link-group")
        .selectChildren("g");
      if (neighbor) {
        nodeGroup
          .filter((d) => neighbor.includes(d.id))
          .selectChildren("circle, rect, .insight-icon")
          .classed(className, enable);
        linkGroup
          .filter((d) => id === d.source.id || id === d.target.id)
          .selectChildren("line,path")
          .classed(className, enable);
      }
      if (type === "selected") {
        nodeGroup
          .filter((d) => d.id === id)
          .selectChildren("circle, rect,.insight-icon")
          .classed("center-highlight", enable);
      }
    },
    crossStatesNeighborHighlight(neighbor, enable, state) {
      const className = "hover-highlight";
      const nodeGroup = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group")
        .select(`.${state}-state`)
        .select(".node-group")
        .selectChildren("g");

      if (neighbor) {
        nodeGroup
          .filter((d) => neighbor.includes(d.id))
          .selectChildren("circle, rect, .insight-icon")
          .classed(className, enable);
      }
    },

    // 构造用于查询邻居的 neighborMap
    getNeighbourInfo(data) {
      const neighborMap = new Map();
      const links = data.links;
      links.forEach((link) => {
        const sourceId = link.source;
        const targetId = link.target;

        if (neighborMap.has(sourceId)) {
          neighborMap.get(sourceId).push(targetId);
        } else {
          neighborMap.set(sourceId, [targetId]);
        }
        if (neighborMap.has(targetId)) {
          neighborMap.get(targetId).push(sourceId);
        } else {
          neighborMap.set(targetId, [sourceId]);
        }
      });
      return neighborMap;
    },

    /* -------------------------------------------------------------------------- */
    // base config
    /* -------------------------------------------------------------------------- */

    simStop() {
      this.simulations.get(this.focusState).stop();
    },

    // rebind data of dom element(nodes and links) and sim system
    restart(hasNewVal, state, newVal) {
      const that = this;
      const nodeIdMap = this.nodeIdMaps.get(state);
      const simulation = this.simulations.get(state);

      /* construct "new" links and nodes  -------------------------------------------------------------------------- */

      const data = newVal === null ? this.selectedData : newVal;

      const links = data.links.map((d) => ({ ...d }));
      let nodes = null;

      if (!hasNewVal) {
        // 获取之前的数据
        const preNodes = simulation.nodes();
        // simple restart, 用旧数据进行更新
        nodes = preNodes.map(function (d) {
          delete d.x;
          delete d.y;
          delete d.vx;
          delete d.vy;
          return d;
        });
      } else {
        // change neighbour highlight and neighbor info
        const selectedNodes = this.selectedNodes;
        const neighborMaps = this.neighborMaps;

        const selectedId = selectedNodes.get(state).id;

        this.neighborHighligt(
          selectedId,
          neighborMaps.get(state).get(selectedId),
          "selected",
          false,
          state
        );
        if (state === this.focusState) {
          this.selectedNode = {
            id: null,
            state: state,
            insightIndex: null,
            "insight-list": null,
            col: null,
            row: null,
          };
          selectedNodes.set(state, this.selectedNode);
        } else {
          selectedNodes.set(state, {
            id: null,
            state: state,
            insightIndex: null,
            "insight-list": null,
          });
          self.filterNode = {
            id: null,
            state: state,
            insightIndex: null,
            "insight-list": null,
          };
        }
        neighborMaps.set(state, this.getNeighbourInfo(newVal));

        // filter of insight
        const originNodeIdMap = this.originNodeIdMaps.get(state);

        const scoreSelectionMap = this.scoreSelectionMaps.get(state);
        // newly filtered value
        nodes = data.nodes.map((id) => {
          const oldNode = nodeIdMap.get(id);

          if (scoreSelectionMap) {
            // filter insight-list
            const originInsightList = originNodeIdMap.get(id)["insight-list"];
            const oldInsightIndexList = oldNode.insightIndexList;
            const oldInsightIndex = oldInsightIndexList[oldNode.insightIndex];
            const newInsightIndexList = [];
            // filter insight-list data
            oldNode["insight-list"] = originInsightList.filter(
              (insight, index) => {
                const type = insight["insight-type"];
                const score = insight["insight-score"];
                const selection = scoreSelectionMap.get(type).selection;
                const selected = scoreSelectionMap.get(type).selected;
                let result = false;
                if (selected) {
                  if (
                    selection === "all" ||
                    (score >= selection[0] && score < selection[1])
                  ) {
                    result = true;
                    newInsightIndexList.push(index);
                  }
                }
                return result;
              }
            );
            const newInsightIndex = newInsightIndexList.findIndex(
              (e) => e === oldInsightIndex
            );
            // reset insight index
            oldNode.insightIndex = newInsightIndex >= 0 ? newInsightIndex : 0;
            oldNode.insightIndexList = newInsightIndexList;
          }
          return oldNode;
        });
      }

      const circleRScale = this.circleRScales.get(state);
      const insightSizeScale = this.insightSizeScales.get(state);
      // recalculate the size of circle and icon
      nodes.forEach((d) => {
        const insightNum = d["insight-list"].length;
        d.circleR = circleRScale(insightNum);
        d.iconSize = insightSizeScale(insightNum);
      });

      const nodeSingleG = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group")
        .select(`.${state}-state`)
        .select("g.node-group");
      const linkSingleG = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group")
        .select(`.${state}-state`)
        .select("g.link-group");

      this.domUpdate(nodes, links, nodeSingleG, linkSingleG, state);
    },

    /* -------------------------------------------------------------------------- */
    // vegaLite relative
    /* -------------------------------------------------------------------------- */
    drawVegaLite(g, mode, state) {
      const that = this;

      const simulation = this.simulations.get(state);
      const showIndex = this.showIndexs.get(state);
      const pinnedIndex = this.pinnedIndexs.get(state);

      const container = g.select(".vega-lite-container");
      const rect = g.selectChild(".rect");
      const removeIcon = g.selectChild(".remove");
      const pinIcon = g.selectChild(".pin");
      const checkIcon = g.selectChild(".check");
      const preView = g.datum().view;
      const rectTitle = g.select(".rect-title");
      const rectTitleName = g.selectChild(".title-name");
      const rectTitleDescription = g.selectChild(".title-description");
      const gData = g.datum();

      if (preView) {
        // reset the view
        const svg = container.selectChild("svg");
        switch (mode) {
          case "img":
            // 创建反应新状态的img
            svg.classed("not-show", true);
            const imgInfo = gData.img;
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
        let yourVlSpec = JSON.parse(
          gData["insight-list"][gData.insightIndex]["vega-lite"]
        );

        // add some options
        yourVlSpec["width"] = this.vegaLiteWidth;
        yourVlSpec["height"] = this.vegaLiteHeight;
        yourVlSpec["usermeta"] = { embedOptions: { renderer: "svg" } };

        // initialization
        vegaEmbed(container.node(), yourVlSpec).then((result) => {
          const view = result.view.background("transparent");
          // record the view
          g.datum().view = view;
          showIndex.set(gData.id, view);

          const linkForce = simulation.force("link");
          if (linkForce) linkForce.initialize(simulation.nodes(), d3.randomLcg);
          const bodyForce = simulation.force("charge");
          if (bodyForce) {
            simulation.force("charge", null);
            simulation.force("charge", bodyForce);
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
          const rectHeight =
            +height + that.rectHeightOffset * 2 + titleHeight + that.iconSize;

          const translateX = rectWidth / 2;
          const translateY = rectHeight / 2;
          g.datum().rect = {
            r: Math.sqrt(Math.pow(translateX, 2) + Math.pow(translateY, 2)),
            width: rectWidth,
            height: rectHeight,
          };
          const collideForce = simulation.force("collide");
          if (collideForce)
            collideForce.initialize(simulation.nodes(), d3.randomLcg);

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
            .text(function () {
              return gData["insight-list"][gData.insightIndex]["insight-type"];
            })
            .attr("x", -translateX + that.iconOffset)
            .attr("y", -translateY + that.iconSize + that.iconOffset / 2)
            .attr("font-size", that.iconSize - 2);
          rectTitleDescription
            .text(function () {
              const rowName = gData.row;

              return `row: ${rowName}`;
            })
            .attr("font-size", "10px")
            .attr("x", -translateX + that.iconOffset)
            .attr("y", -translateY + that.iconSize + titleHeight)
            .append("tspan")
            .attr("x", -translateX + that.iconOffset)
            .attr("dy", "1.2em")
            .style("text-align", "left")
            .text(function () {
              const colName = gData.col;
              return `col: ${colName}`;
            });
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
          checkIcon.attr(
            "transform",
            `translate(${
              translateX - 3 * that.iconSize - that.iconOffset - 2
            },${-translateY + that.iconOffset})`
          );

          if (g.datum().checked) {
            checkIcon.classed("icon-pinned", true);
          }

          switch (mode) {
            case "img":
              // 创建反应新状态的img
              svg.classed("not-show", true);
              const imgInfo = gData.img;
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
                g.select("image")
                  .attr("opacity", 0)
                  .transition()
                  .duration(175)
                  .attr("opacity", 1);
              });
              break;
            case "svg":
              // 初始就设置为 pinned 状态
              pinIcon.classed("icon-pinned", true);
              pinnedIndex.set(gData.id, g);
              g.datum().pinned = true;
              g.classed("pinned", true);
              g.datum().fx = gData.x;
              g.datum().fy = gData.y;
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
      that.simulationRestart(simulation);
    },
    deleteVegaLite(g, state) {
      const showIndex = this.showIndexs.get(state);
      const pinnedIndex = this.pinnedIndexs.get(state);

      const id = g.datum().id;
      showIndex.get(id).finalize();
      g.selectAll(".vega-lite-graph").remove();
      g.datum().view = null;
      g.datum().img = null;

      pinnedIndex.delete(id);
      showIndex.delete(id);
    },
    /* -------------------------------------------------------------------------- */
    // other
    /* -------------------------------------------------------------------------- */

    getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    },

    // createObserver(svgElement) {
    //   // 创建 ResizeObserver 实例
    //   const observer = new ResizeObserver((entries) => {
    //     // 遍历所有被观察的元素
    //     for (let entry of entries) {
    //       const { width, height } = entry.contentRect;
    //       this.width = width;
    //       this.height = height;
    //       this.rightCornerCoord = [width, height];

    //       this.zoom.translateExtent([
    //         [-width, -height],
    //         [width * 2, height * 2],
    //       ]);
    //       const defaultForceConfig = this.defaultForceConfig;
    //       this.simulation
    //         .force(
    //           "center",
    //           d3
    //             .forceCenter(width / 2, height / 2)
    //             .strength(defaultForceConfig.center.Strength)
    //         )
    //         .force(
    //           "x",
    //           d3
    //             .forceX()
    //             .x(width / 2)
    //             .strength(defaultForceConfig.x.Strength)
    //         )
    //         .force(
    //           "y",
    //           d3
    //             .forceY()
    //             .y(height / 2)
    //             .strength(defaultForceConfig.y.Strength)
    //         );

    //       this.restart(false);
    //     }
    //   });
    //   // 开始观察 SVG 元素
    //   observer.observe(svgElement);
    // },
    // initialization of focus graph, create DOM elements and sim system
    drawGraph(newVal) {
      const that = this;

      const neighborMap = this.getNeighbourInfo(newVal);

      this.showIndexs.set(this.focusState, this.showIndex);
      this.hoverIndexs.set(this.focusState, this.hoverIndex);
      this.checkIndexs.set(this.focusState, this.checkIndex);
      this.selectedNodes.set(this.focusState, this.selectedNode);
      this.pinnedIndexs.set(this.focusState, this.pinnedIndex);
      this.neighborMaps.set(this.focusState, neighborMap);

      const showIndex = this.showIndex;
      const hoverIndex = this.hoverIndex;
      const checkIndex = this.checkIndex;
      const pinnedIndex = this.pinnedIndex;

      // 获取绘画数据
      const originNodes = this.nodeStateMaps.get(this.focusState);
      const links = newVal.links.map((d) => ({ ...d }));

      // 创建每个node insight num到 circleR & insight icon size的映射
      const [circleRScale, insightSizeScale] =
        this.getSvgInnterSizeScale(originNodes);

      this.circleRScales.set(this.focusState, circleRScale);
      this.insightSizeScales.set(this.focusState, insightSizeScale);

      // 加入更多属性，控制vega-lite图的显示
      const nodes = originNodes.map((d) => {
        const insightNum = d["insight-list"].length;
        return {
          ...d,
          insightIndex: 0,
          insightIndexList: [...Array(insightNum).keys()],
          circleR: circleRScale(insightNum),
          iconSize: insightSizeScale(insightNum),
          showDetail: false,
          pinned: false,
          checked: false,
          view: null,
          img: null,
          rect: null,
        };
      });
      const nodeIdMap = new Map();
      nodes.forEach((node) => {
        nodeIdMap.set(node.id, node);
      });

      this.nodeIdMaps.set(this.focusState, nodeIdMap);
      // 选择svg container
      const svgContainer = d3.select("#force-svg-container");

      // // 清除之前的
      // svgContainer.selectAll("*").remove();

      // 获取container的宽和高
      const width = this.containerWidth;
      const height = this.containerHeight;

      // 选择top node g
      const gTop = svgContainer
        .select("#total-svg")
        .selectChild("g.node-group");

      const svg = gTop.select(`svg.${this.focusState}-state`);

      // 设置svg 宽和高 (根据 nodeNum属性)
      this.updateSvgSize(svg, this.svgRScale, this.maxNodeNum);
      const center = svg.datum().viewBoxR / 2;

      svg
        .classed("focus-svg", true)
        .attr("fill", "#fff")
        .attr("overflow", "visible");

      svg.datum().pinned = true;
      svg.datum().fx = width * 0.5;
      svg.datum().fy = height * 0.5;

      this.svgNodeDatas.set(this.focusState, svg.datum());

      const backgroundShape = svg
        .append("rect")
        .attr("class", "background-shape")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", "100%")
        .attr("height", "100%")
        .on("dblclick", function () {
          const svgData = d3.select(this.parentNode).datum();
          svgData.pinned = !svgData.pinned;
          if (svgData.pinned) {
            svgData.fx = svgData.x;
            svgData.fy = svgData.y;
          } else {
            svgData.fx = null;
            svgData.fy = null;
          }
        })
        .on("dblclick.zoom", function (event) {
          event.preventDefault();
          event.stopPropagation();
        });

      // this.createObserver(svg.node());
      //data binding

      const linkG = svg
        .append("g")
        .attr("class", "link-group")
        .selectAll("g")
        .data(links, (d) => {
          if (typeof d.source === "object") {
            return `${d.source.id}_${d.target.id}`;
          } else {
            return `${d.source}_${d.target}`;
          }
        })
        .join("g");

      const circleG = svg
        .append("g")
        .attr("class", "node-group")
        .selectAll("g")
        .data(nodes, (d) => d.id)
        .join("g");

      this.addSvgIcon(svg, "amplify");

      const stateText = svg
        .append("text")
        .attr("class", "state-text")
        .text(this.focusState)
        .attr("font-size", (d) => d.viewBoxR / 14)
        .attr("font-weight", "bold")
        .attr("text-anchor", "end")
        .attr("dominant-baseline", "hanging")
        .style("fill", "#9CA0AD")
        .attr("x", "99%")
        .attr("y", "1%");
      /* -------------------------------------------------------------------------- */

      const ticked = this.createTickFunction(svg);
      const simulation = this.createForceSimulation(
        nodes,
        links,
        ticked,
        neighborMap,
        showIndex,
        center
      );
      this.simulations.set(this.focusState, simulation);

      this.setDomAttributes(linkG, circleG, this.focusState);

      this.addZoomBehavior(svg, simulation);
      // // initialize the default data
      // this.defaultForceConfig.center.X =
      //   this.defaultForceConfig.x.X =
      //   this.defaultForceConfig.radial.X =
      //     boundaryR;

      // this.defaultForceConfig.center.Y =
      //   this.defaultForceConfig.y.Y =
      //   this.defaultForceConfig.radial.Y =
      //     boundaryR;
    },
    drawSubGraph(graphInfo) {
      const that = this;
      const state = graphInfo.state;
      const data = graphInfo.data;
      const originNodes = this.nodeStateMaps.get(state);

      // 创建每个node insight num到 circleR & insight icon size的映射
      const [circleRScale, insightSizeScale] =
        this.getSvgInnterSizeScale(originNodes);
      this.circleRScales.set(state, circleRScale);
      this.insightSizeScales.set(state, insightSizeScale);
      // 获取内部nodes和links数据
      let links = data.links.map((d) => ({ ...d }));
      let nodes = originNodes.map((d) => {
        const insightNum = d["insight-list"].length;
        return {
          ...d,
          insightIndex: 0,
          insightIndexList: [...Array(insightNum).keys()],
          circleR: circleRScale(insightNum),
          iconSize: insightSizeScale(insightNum),
          showDetail: false,
          pinned: false,
          checked: false,
          view: null,
          img: null,
          rect: null,
        };
      });
      // 创建 id map，便于查询数据
      const nodeIdMap = new Map();
      nodes.forEach((node) => {
        nodeIdMap.set(node.id, node);
      });
      this.nodeIdMaps.set(state, nodeIdMap);

      // 创建辅助数据类型，全部根据state索引
      const showIndex = new Map();
      const hoverIndex = {
        id: null,
        col: null,
        row: null,
      };
      const checkIndex = new Map();
      const pinnedIndex = new Map();
      const selectedNode = {
        id: null,
        state: state,
        insightIndex: null,
        "insight-list": null,
        col: null,
        row: null,
      };
      const neighborMap = this.getNeighbourInfo(data);

      this.showIndexs.set(state, showIndex);
      this.hoverIndexs.set(state, hoverIndex);
      this.checkIndexs.set(state, checkIndex);
      this.selectedNodes.set(state, selectedNode);
      this.pinnedIndexs.set(state, pinnedIndex);
      this.neighborMaps.set(state, neighborMap);

      // 选择顶层svg下的g.node-group和对应的子svg
      const gTop = d3
        .select("#force-svg-container")
        .select("#total-svg")
        .selectChild("g.node-group");
      const svg = gTop.select(`svg.${state}-state`);

      // 更新svg 宽高

      this.updateSvgSize(svg, this.svgRScale, 0);
      const center = svg.datum().viewBoxR / 2;

      svg.attr("overflow", "visible");

      // 设置svg子元素的绑定的data属性
      svg.datum().pinned = false;

      this.svgNodeDatas.set(state, svg.datum());

      // 添加背景rect元素
      const backgroundShape = svg
        .append("rect")
        .attr("class", "background-shape")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", "100%")
        .attr("height", "100%")
        .on("dblclick", function () {
          const svgData = d3.select(this.parentNode).datum();
          svgData.pinned = !svgData.pinned;
          if (svgData.pinned) {
            svgData.fx = svgData.x;
            svgData.fy = svgData.y;
          } else {
            svgData.fx = null;
            svgData.fy = null;
          }
        })
        .on("dblclick.zoom", function (event) {
          event.preventDefault();
          event.stopPropagation();
        });

      /* -------------------------------------------------------------------------- */
      // 开始生成对应的DOM元素
      // 先绑定空数据，对应nodeNum为0
      nodes = [];
      links = [];

      // 创建顶层g元素 (nodeG 和 linkG)
      const linkG = svg
        .append("g")
        .attr("class", "link-group")
        .selectAll("g")
        .data(links, (d) => {
          if (typeof d.source === "object") {
            return `${d.source.id}_${d.target.id}`;
          } else {
            return `${d.source}_${d.target}`;
          }
        })
        .join("g");

      const circleG = svg
        .append("g")
        .attr("class", "node-group")
        .selectAll("g")
        .data(nodes, (d) => d.id)
        .join("g");

      // 顶层 icon
      this.addSvgIcon(svg, "focus");
      // 顶层 text
      const stateText = svg
        .append("text")
        .attr("class", "state-text")
        .text(state)
        .attr("font-size", (d) => d.viewBoxR / 12)
        .attr("font-weight", "bold")
        .attr("text-anchor", "end")
        .attr("dominant-baseline", "hanging")
        .style("fill", "#9CA0AD")
        .attr("x", "99%")
        .attr("y", "1%");

      /* -------------------------------------------------------------------------- */
      //力导向系统创建;
      // const oldBoundaryRect = [
      //   boundary[0],
      //   boundary[1],
      //   boundary[2] + boundary[0],
      //   boundary[3] + boundary[1],
      // ];
      // const boundaryRect = [
      //   boundary[0],
      //   boundary[1],
      //   boundary[2] + boundary[0],
      //   boundary[3] + boundary[1],
      // ];
      const ticked = this.createTickFunction(svg);
      const simulation = this.createForceSimulation(
        nodes,
        links,
        ticked,
        neighborMap,
        showIndex,
        center
      );
      this.simulations.set(state, simulation);
      /* -------------------------------------------------------------------------- */
      // DOM元素创建
      this.setDomAttributes(linkG, circleG, state);
      /* -------------------------------------------------------------------------- */
      // Zoom 添加
      this.addZoomBehavior(svg, simulation);
    },
    addZoomBehavior(svg, simulation) {
      const that = this;
      // 设置整体zoom行为,只选择最顶层的2个g即可
      const group = svg.selectChildren("g");

      // 创建缩放函数
      const zoom = d3
        .zoom()
        .scaleExtent([0.3, 8]) // 设置缩放的范围
        .on("zoom", zoomed)
        .filter((event) => {
          return event.shiftKey;
        });

      // 仅将缩放行为应用到顶层元素/
      svg.call(zoom);
      // 记录zoom的引用
      this.zooms.set(svg.datum().id, zoom);
      // 定义zoom的回调函数
      function zoomed(event, d) {
        const transform = event.transform;

        // 更新地理路径组的变换属性
        group.attr("transform", transform);
        // change boundary coord
        [d.boundaryRectTmp[0], d.boundaryRectTmp[1]] = transform.invert([0, 0]);
        [d.boundaryRectTmp[2], d.boundaryRectTmp[3]] = transform.invert([
          d.viewBoxR,
          d.viewBoxR,
        ]);

        const newCenterCoord = [
          (d.boundaryRectTmp[0] + d.boundaryRectTmp[2]) / 2,
          (d.boundaryRectTmp[1] + d.boundaryRectTmp[3]) / 2,
        ];

        that.updatePositionForce(simulation, newCenterCoord);

        that.globalSimulation.restart();
      }
    },
    updatePositionForce(simulation, centerCoord) {
      // change position force
      simulation.force("x").x(centerCoord[0]);
      simulation.force("y").y(centerCoord[1]);
      simulation.force("center").x(centerCoord[0]).y(centerCoord[1]);
      this.simulationRestart(simulation);
    },
    createTickFunction(svg) {
      const that = this;
      const boundaryRect = svg.datum().boundaryRectTmp;

      return function ticked() {
        that.globalSimulation.restart();
        // 只通过transform.translate 更新父元素g的位置

        if (!that.amplifyMode) {
          svg
            .select(".node-group")
            .selectChildren("g")
            .style("transform", (d) => {
              if (d.x < boundaryRect[0]) {
                d.x = boundaryRect[0];
              } else if (d.x > boundaryRect[2]) {
                d.x = boundaryRect[2];
              }

              if (d.y < boundaryRect[1]) {
                d.y = boundaryRect[1];
              } else if (d.y > boundaryRect[3]) {
                d.y = boundaryRect[3];
              }

              return `translate(${d.x}px,${d.y}px)`;
            });
        } else {
          svg
            .select(".node-group")
            .selectChildren("g")
            .style("transform", (d) => `translate(${d.x}px,${d.y}px)`);
        }
        // 更新line位置
        svg
          .select(".link-group")
          .selectChildren("g")
          .selectChildren(".network-line")
          .attr("x1", function () {
            const d = d3.select(this.parentNode).datum();
            return d.source.x;
          })
          .attr("y1", function () {
            const d = d3.select(this.parentNode).datum();
            return d.source.y;
          })
          .attr("x2", function () {
            const d = d3.select(this.parentNode).datum();
            return d.target.x;
          })
          .attr("y2", function () {
            const d = d3.select(this.parentNode).datum();
            return d.target.y;
          });
        // 更新锥形位置(如果有)
        svg
          .select(".link-group")
          .selectChildren("g")
          .selectChildren("path.network-angle")
          .attr("d", function () {
            const d = d3.select(this.parentNode).datum();
            let point1 = [];
            let point2 = [];
            const name1 = d.source.id;
            const name2 = d.target.id;
            if (name1.length < name2.length) {
              point1 = [d.source.x, d.source.y];
              point2 = [d.target.x, d.target.y];
            } else {
              point1 = [d.target.x, d.target.y];
              point2 = [d.source.x, d.source.y];
            }

            const widthAtStart = 15;
            const widthAtEnd = 1;

            const angle = Math.atan2(
              point2[1] - point1[1],
              point2[0] - point1[0]
            );

            const p1 = [
              point1[0] + widthAtStart * Math.sin(angle),
              point1[1] - widthAtStart * Math.cos(angle),
            ];

            const p2 = [
              point1[0] - widthAtStart * Math.sin(angle),
              point1[1] + widthAtStart * Math.cos(angle),
            ];

            const p3 = [
              point2[0] - widthAtEnd * Math.sin(angle),
              point2[1] + widthAtEnd * Math.cos(angle),
            ];

            const p4 = [
              point2[0] + widthAtEnd * Math.sin(angle),
              point2[1] - widthAtEnd * Math.cos(angle),
            ];

            return `M${p1} L${p2} L${p3} L${p4} Z`;
          });
      };
    },
    drawGlobalGraph(newVal) {
      const that = this;

      /* -------------------------------------------------------------------------- */
      // 设置top svg 宽高属性
      const svgContainer = d3.select("#force-svg-container");
      const width = parseInt(svgContainer.style("width"), 10);
      const height = parseInt(svgContainer.style("height"), 10);

      const svgTop = svgContainer
        .select("#total-svg")
        .attr("viewBox", [0, 0, width, height]);

      /* -------------------------------------------------------------------------- */
      // 添加top g，用于global zoom和 bundle g的管理
      const linkGTop = svgTop.append("g").attr("class", "link-group");
      const nodeGTop = svgTop.append("g").attr("class", "node-group");
      const bundleGTop = svgTop.append("g").attr("class", "bundle-group");
      const groupsTop = svgTop.selectChildren("g.link-group,g.node-group");
      // const groupsTop = svgTop.selectChildren("g");

      svgTop
        .append("use")
        .attr("href", "#defs-shrink")
        .attr("class", "shrink-icon")
        .attr("x", 0)
        .attr("y", 5)
        .attr("width", "6%")
        .attr("height", "6%")
        .style("color", "transparent")
        .attr("cursor", "pointer")
        .classed("not-show", true)
        .on("click", function () {
          that.amplifyMode = false;
          that.enterAmplifyMode(that.focusState, false);
          that.globalSimulation.restart();
          that.simulations.get(that.focusState).restart();
        })
        .on("mouseover", function () {
          d3.select(this)
            .classed("hover-highlight", true)
            .style("color", "#8d93a7");
        })
        .on("mouseleave", function () {
          d3.select(this)
            .classed("hover-highlight", false)
            .style("color", "transparent");
        });

      /* -------------------------------------------------------------------------- */
      // svg子图初步生成
      // 生成全局力道图对应的nodes和links数据
      const svgData = Array.from(newVal.entries()).map((stateInfo) => ({
        id: stateInfo[0],
        nodeNum: stateInfo[1].nodes.length,
      }));

      const svgLinks = Array.from(newVal.keys()).map((state) => ({
        source: this.focusState,
        target: state,
      }));
      svgLinks.shift();

      this.svgLinkDatas.push(...svgLinks);

      // 绑定顶层svg与links数据到对应的g中，生成子svg元素和state links
      const svgGroups = nodeGTop
        .selectChildren("svg")
        .data(svgData)
        .join("svg")
        .attr("class", (d) => `${d.id}-state`)
        .attr("preserveAspectRatio", "xMinYMin meet");

      const linkGroups = linkGTop
        .selectAll("line")
        .data(svgLinks, (d) => {
          if (typeof d.source === "object") {
            return `${d.source.id}_${d.target.id}`;
          } else {
            return `${d.source}_${d.target}`;
          }
        })
        .join("line")
        .attr("class", (d) => {
          return `${d.source}_${d.target}`;
        })
        // .attr("stroke", "#000");
        .attr("stroke", "none");

      /* -------------------------------------------------------------------------- */
      // 生成子svg图具体内容
      for (let [state, data] of newVal) {
        if (state === this.focusState) {
          // 针对focus state，提交数据，生成左侧 control panel需要的数据，并生成子svg图内容
          const focusLinks = data.links;
          const nodesData = this.nodeStateMaps.get(state);

          const originNodeIdMap = new Map();

          nodesData.forEach((d) => {
            originNodeIdMap.set(d.id, d);
          });
          this.originNodeIdMaps.set(state, originNodeIdMap);
          this.updateSvgSize(
            nodeGTop.select(`svg.${this.focusState}-state`),
            this.svgRScale,
            this.maxNodeNum
          );

          this.$store.dispatch("force/setStatisticGraph", {
            state: state,
            data: {
              nodes: nodesData,
              links: focusLinks,
            },
          });
        } else {
          // 非focus state的内容生成
          const subNodes = data.nodes;
          const subLinks = data.links;

          this.drawSubGraph({
            state: state,
            data: {
              nodes: subNodes,
              links: subLinks,
            },
          });
        }
      }

      /* -------------------------------------------------------------------------- */
      // 全局力道图布局 + zoom + drag 定义，必须要在子svg图生成之后
      // 创建全局zoom
      const zoomTop = d3
        .zoom()
        .scaleExtent([0.1, 8]) // 设置缩放的范围
        .on("zoom", zoomedTop)
        .filter((event) => {
          return (
            event.target === svgTop.node() ||
            nodeGTop
              .selectChildren("svg")
              .select(".background-shape")
              .nodes()
              .includes(event.target)
          );
        });
      svgTop.call(zoomTop);

      // 创建顶层svg drag
      const dragDefine = d3
        .drag()
        .container(function () {
          // 选择顶层nodeGy元素作为容器，影响 event.x和event.y
          return nodeGTop.node();
        })
        .filter((event) => !event.shiftKey)
        .on("start", dragstartedSvg)
        .on("drag", draggedSvg)
        .on("end", dragendedSvg);

      svgGroups.call(dragDefine);
      this.globalDragDefine = dragDefine;

      // 创建全局力道图布局
      const defaultBaseConfig = this.defaultBaseConfig;
      const defaultForceConfig = this.defaultForceConfig;
      const globalSimulation = d3
        .forceSimulation(svgData)
        .force(
          "link",
          d3
            .forceLink(svgLinks)
            .id((d) => d.id)
            //.distance(width / 3)
            .distance((d) => {
              const nodeNumS = d.source.nodeNum;
              const nodeNumT = d.target.nodeNum;

              return (
                this.linkDistanceScale(nodeNumS) +
                this.linkDistanceScale(nodeNumT)
              );
            })
        )
        .force(
          "charge",
          d3
            .forceManyBody()
            .strength((d) => this.chargeStrengthScale(d.nodeNum))
            .theta(defaultForceConfig.manyBody.Theta)
            .distanceMin(defaultForceConfig.manyBody.DistanceMin)
        )
        .alpha(defaultBaseConfig.alpha)
        .alphaMin(defaultBaseConfig.alphaMin)
        .alphaTarget(defaultBaseConfig.alphaTarget)
        .alphaDecay(defaultBaseConfig.alphaDecay)
        .velocityDecay(defaultBaseConfig.velocityDecay)
        .on("tick", globalTicked);
      this.globalSimulation = globalSimulation;

      // create bundle generator
      const lineGenerator = d3
        .line()
        .x((d) => d.x)
        .y((d) => d.y)
        // .curve(d3.curveCardinal.tension(1));
        .curve(d3.curveBundle.beta(1));

      function globalTicked() {
        // 移动svg时，由于左上角是x，y坐标，要记得减去高和宽的偏移
        nodeGTop.selectChildren("svg").attr("x", (d) => d.x - d.width / 2);
        nodeGTop.selectChildren("svg").attr("y", (d) => d.y - d.height / 2);
        linkGTop
          .selectChildren("line")
          .attr("x1", (d) => d.source.x)
          .attr("y1", (d) => d.source.y)
          .attr("x2", (d) => d.target.x)
          .attr("y2", (d) => d.target.y);

        const zoomTransform = d3.zoomTransform(svgTop.node());

        bundleGTop.selectChildren("path").attr("d", (d) => {
          const sourceSvgElement = nodeGTop
            .select(`.${d.source.state}-state`)
            .node();
          const targetSvgElement = nodeGTop
            .select(`.${d.target.state}-state`)
            .node();
          const sourceMartix = getTransformationMatrix(
            sourceSvgElement,
            svgTop.node()
          );
          const targetMartix = getTransformationMatrix(
            targetSvgElement,
            svgTop.node()
          );

          const sourcePointOrigin = [d.source.x, d.source.y];
          const targetPointOrigin = [d.target.x, d.target.y];
          // const sourcePointOrigin = sourceSvgElement.createSVGPoint();
          // sourcePointOrigin.x = d.source.x;
          // sourcePointOrigin.y = d.source.y;

          const sourcePoint = getClosetRectPoint(
            sourcePointOrigin,
            targetPointOrigin,
            sourceMartix,
            targetMartix,
            d.source,
            sourceSvgElement
          );

          const targetPoint = getClosetRectPoint(
            targetPointOrigin,
            sourcePointOrigin,
            targetMartix,
            sourceMartix,
            d.target,
            sourceSvgElement
          );
          // const targetPointOrigin = targetSvgElement.createSVGPoint();
          // targetPointOrigin.x = d.target.x;
          // targetPointOrigin.y = d.target.y;

          return lineGenerator([
            {
              x: sourcePoint.x,
              y: sourcePoint.y,
            },
            {
              x: zoomTransform.applyX(
                (d.middle.source.x + d.middle.target.x) / 2
              ),
              y: zoomTransform.applyY(
                (d.middle.source.y + d.middle.target.y) / 2
              ),
            },
            {
              x: zoomTransform.applyX(
                (d.middle.source.x + d.middle.target.x * 2) / 3
              ),
              y: zoomTransform.applyY(
                (d.middle.source.y + d.middle.target.y * 2) / 3
              ),
            },
            {
              x: targetPoint.x,
              y: targetPoint.y,
            },
          ]);
        });
      }

      function getTransformedPoint(p, martix, svg) {
        const point = svg.createSVGPoint();
        point.x = p.x;
        point.y = p.y;
        return point.matrixTransform(martix);
      }
      function getClosetRectPoint(point1, point2, martix1, martix2, d, svg) {
        const rectInfo = d.rect;

        const res = { x: point1[0], y: point1[1] };
        const p1 = getTransformedPoint(
          { x: point1[0], y: point1[1] },
          martix1,
          svg
        );
        if (d.showDetail) {
          const p2 = getTransformedPoint(
            { x: point2[0], y: point2[1] },
            martix2,
            svg
          );
          const rectPoint1 = getTransformedPoint(
            {
              x: point1[0] - rectInfo.width / 2,
              y: point1[1] - rectInfo.height / 2,
            },
            martix1,
            svg
          );
          const rectPoint2 = getTransformedPoint(
            {
              x: point1[0] + rectInfo.width / 2,
              y: point1[1] + rectInfo.height / 2,
            },
            martix1,
            svg
          );

          const transformedWidth = rectPoint2.x - rectPoint1.x;
          const transformedHeight = rectPoint2.y - rectPoint1.y;
          const dx = p2.x - p1.x;
          const dy = p2.y - p1.y;

          if (dx * transformedHeight > dy * transformedWidth) {
            if (dx * transformedHeight > -dy * transformedWidth) {
              res.x = point1[0] + rectInfo.width / 2;
            } else {
              res.y = point1[1] - rectInfo.height / 2;
            }
          } else {
            if (dx * transformedHeight > -dy * transformedWidth) {
              res.y = point1[1] + rectInfo.height / 2;
            } else {
              res.x = point1[0] - rectInfo.width / 2;
            }
          }
        }
        return getTransformedPoint({ x: res.x, y: res.y }, martix1, svg);
      }
      function getTransformationMatrix(childSVGElement, parentSVGElement) {
        // 获取d3的缩放转换
        let zoomTransform = d3.zoomTransform(childSVGElement);
        let zoomMatrix = childSVGElement
          .createSVGMatrix()
          .translate(zoomTransform.x, zoomTransform.y)
          .scale(zoomTransform.k);

        // 获取子 SVG 到屏幕的转换矩阵
        let childToScreenMatrix = childSVGElement.getScreenCTM();

        // 获取屏幕到父 SVG 的转换矩阵
        let screenToParentMatrix = parentSVGElement.getScreenCTM().inverse();

        // 计算总的转换矩阵
        let totalMatrix = screenToParentMatrix
          .multiply(childToScreenMatrix)
          .multiply(zoomMatrix);

        return totalMatrix;
      }

      function zoomedTop(event) {
        const transform = event.transform;
        // 更新地理路径组的变换属性
        groupsTop.attr("transform", transform);
        that.globalSimulation.restart();
      }
      function dragstartedSvg(event) {
        if (!event.active)
          that.globalSimulation
            .alphaTarget(
              +that.defaultBaseConfig.alphaTarget + 0.3 > 1
                ? 1
                : +that.defaultBaseConfig.alphaTarget + 0.3
            )
            .restart();

        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
      }

      // 拖动时，让点跟着鼠标走
      function draggedSvg(event) {
        // 更新节点位置
        event.subject.fx = event.x;
        event.subject.fy = event.y;
      }

      // 拖动结束，降温
      function dragendedSvg(event) {
        if (!event.active)
          that.globalSimulation.alphaTarget(that.defaultBaseConfig.alphaTarget);

        if (event.subject.pinned) {
          event.subject.fx = event.subject.x;
          event.subject.fy = event.subject.y;
        } else {
          event.subject.fx = null;
          event.subject.fy = null;
        }
      }
    },

    // force function
    createForceSimulation(
      nodes,
      links,
      ticked,
      neighborMap,
      showIndex,
      center
    ) {
      const defaultBaseConfig = this.defaultBaseConfig;
      const defaultForceConfig = this.defaultForceConfig;
      const that = this;
      const simulation = d3
        .forceSimulation(nodes)
        .force(
          "link",
          d3
            .forceLink(links)
            // 指明对应的是nodes数据的id属性
            .id((d) => d.id)
            // .distance(defaultForceConfig.link.Distance)
            .distance(function (d) {
              const sourceId = d.source.id;
              const targetId = d.target.id;

              const neighbor1 = neighborMap.get(sourceId);
              const neighbor2 = neighborMap.get(targetId);
              let neighborCount1 = 0;
              let neighborCount2 = 0;
              if (neighbor1) neighborCount1 = neighbor1.length;
              if (neighbor2) neighborCount2 = neighbor2.length;

              let distanceIncrease = 5;
              if (neighborCount1 > 3 && neighborCount2 > 3) {
                distanceIncrease = 20;
              } else if (neighborCount1 > 3 || neighborCount2 > 3) {
                distanceIncrease = 0;
              }

              const circleR1 = d.source.circleR;
              const circleR2 = d.target.circleR;
              const middleR = that.circleR * 1.5;
              if (circleR1 > middleR || circleR2 > middleR) {
                distanceIncrease += 25;
                if (circleR1 > middleR && circleR2 > middleR)
                  distanceIncrease += 25;
              }

              if (showIndex.size > 0) {
                const show1 = showIndex.has(d.source.id);
                const show2 = showIndex.has(d.target.id);
                if (show1 || show2) {
                  if (show1 && show2) {
                    return that.vegaLiteLongLink + distanceIncrease;
                  } else {
                    return that.vegaLiteLink + distanceIncrease;
                  }
                }

                for (const id of showIndex.keys()) {
                  const directNeighbor = neighborMap.get(id);
                  if (directNeighbor) {
                    for (const neighbor of directNeighbor) {
                      const secondNeighbor = neighborMap.get(neighbor);
                      if (
                        (targetId === neighbor &&
                          secondNeighbor.includes(sourceId)) ||
                        (sourceId === neighbor &&
                          secondNeighbor.includes(targetId))
                      ) {
                        return that.circleNeighborLink + distanceIncrease;
                      }
                    }
                  }
                }
              }

              return that.circleLink + distanceIncrease;
            })
            .iterations(defaultForceConfig.link.Iterations)
          // .strength(defaultForceConfig.link.Strength)
        )
        .force(
          "charge",
          d3
            .forceManyBody()
            .strength(function (d) {
              let forceIncrease = 0;
              const circleR = d.circleR;
              const middleR = that.circleR * 1.5;
              if (circleR > middleR) {
                forceIncrease = -100;
              }

              let strength = that.circleStrength;
              if (d.showDetail) {
                strength = that.vegaLiteStrength;
              } else {
                if (showIndex.size > 0) {
                  const id = d.id;
                  for (const showId of showIndex.keys()) {
                    const directNeighbor = neighborMap.get(showId);
                    if (directNeighbor) {
                      for (const neighbor of directNeighbor) {
                        const secondNeighbor = neighborMap.get(neighbor);
                        if (secondNeighbor.includes(id)) {
                          return that.circleNeighborStrength + forceIncrease;
                        }
                      }
                    }
                  }
                }
              }

              return strength + forceIncrease;
            })
            .theta(defaultForceConfig.manyBody.Theta)
            .distanceMin(defaultForceConfig.manyBody.DistanceMin)
          // .distanceMax(defaultForceConfig.manyBody.DistanceMax)
        )
        .force(
          "center",
          d3
            .forceCenter(center, center)
            .strength(defaultForceConfig.center.Strength)
        )
        .force(
          "x",

          d3.forceX().x(center).strength(defaultForceConfig.x.Strength)
        )
        .force(
          "y",

          d3.forceY().y(center).strength(defaultForceConfig.y.Strength)
        )
        .force(
          "collide",
          d3
            .forceCollide((d) => {
              if (d.showDetail) {
                return d.rect.r;
              } else {
                return d.circleR;
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

      return simulation;
    },
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

#force-svg-container {
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
  width: 20rem;
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

.more-icon {
  fill: #545b77;
  cursor: pointer;
  width: 2.5rem;
  height: 2.5rem;
}

.more-box {
  position: fixed;
  top: 7%;
  right: 1%;
}
.showMorePanelBox {
  position: absolute;
  top: 0;
  right: 0;
}
.ticks-card {
  position: fixed;
  top: 5%;
  right: 2%;
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
  box-shadow: inset 0.2rem 0.2rem 1.6rem #4444442a, inset -0.2rem -0.2rem 1.6rem #4444442a;
}

.btn {
  border-radius: 1.2rem;
}
</style>

<style lang="less" scoped>
.el-slider {
  width: 100%;
}
.bugfix {
  margin-top: 1rem;
}
</style>

<!-- Animation -->
<style scoped>
.slide-enter-active {
  transition: all 70ms ease-out;
}

.slide-leave-active {
  transition: all 70ms ease-in;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(20rem); /* 初始状态和最终状态 */
}

.slide-enter-to,
.slide-leave-from {
  transform: translateX(0); /* 平移隐藏 */
}
</style>

<!-- global style -->
<style lang="less">
.shrink-icon,
.focus-icon {
  fill: #8d93a7;
  transition: color 0.2s, fill 0.2s;
  &.hover-highlight {
    fill: #fff;
  }
}
.normal-circle {
  stroke: none;
}
#total-svg {
  .node-group {
    .background-shape {
      fill: #fff;
      filter: url(#rect-shadow);
    }
    .focus-svg {
      .background-shape {

        filter: url(#rect-shadow-focus);
      }
    }
  }
}

.circle,
.rect,
.rect-title {
  &.hover-highlight {
    //stroke: #f98585;
    stroke: #aaa;
    stroke-width: 2.5px;
  }
  &.selected-highlight {
    stroke: #71627a;
    stroke-width: 2.5px;
  }
  &.center-highlight {
    stroke: #22b8cf;
    stroke-width: 3px;
  }
}
.insight-icon,
.circle {
  &.hover-highlight {
    transform: scale(1.4);
  }
}

.network-line {
  &.hover-highlight,
  &.selected-highlight,
  &.center-highlight {
    stroke-width: 3.5px;
  }
}

.network-angle {
  &.hover-highlight,
  &.selected-highlight,
  &.center-highlight {
    fill: #999;
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
.svg {
  width: 100%;
}

rect.svg-inset {
  stroke: #545b77 !important;

  // stroke-opacity: 0.7;
  stroke-width: 5 !important;
  // filter: url(#inset-shadow);
}

circle.svg-inset {
  stroke: #545b77 !important;
  stroke-width: 5px !important;

  // filter: url(#inset-shadow-circle);
  //  stroke-width: 0 !important;
}
</style>
