class HQPillow:
    # Inverses the colors of the image
    def inverse(self):
        rgb_image = self.convert('RGB')

        for x in range(0, self.width):
            for y in range(0, self.height):
                (r, g, b) = rgb_image.getpixel((x, y))

                self.putpixel((x, y), (255 - r, 255 - g, 255 - b))

    # Merges 2 images of the same size. Note that it will not work if they are not the same size
    def combine(self, image2):
        rgb_image1 = self.convert('RGB')
        rgb_image2 = image2.convert('RGB')

        for x in range(0, self.width):
            for y in range(0, self.height):
                (r1, g1, b1) = rgb_image1.getpixel((x, y))
                (r2, g2, b2) = rgb_image2.getpixel((x, y))

                self.putpixel((x, y), (int((r1 + r2) / 2), int((g1 + g2) / 2), int((b1 + b2) / 2)))

    # Turns the image red based on an input percentage
    def redshift(self, percent):
        if percent > 100:
            percent = 100

        rgb_image = self.convert('RGB')

        for x in range(0, self.width):
            for y in range(0, self.height):
                (r, g, b) = rgb_image.getpixel((x, y))

                self.putpixel((x, y), (r, int(g * (percent / 100)), int(b * (percent / 100))))

    # Turns the image green based on an input percentage
    def greenshift(self, percent):
        if percent > 100:
            percent = 100

        rgb_image = self.convert('RGB')

        for x in range(0, self.width):
            for y in range(0, self.height):
                (r, g, b) = rgb_image.getpixel((x, y))

                self.putpixel((x, y), (int(r * (percent / 100)), g, int(b * (percent / 100))))

    # Turns the image blue based on an input percentage
    def blueshift(self, percent):
        if percent > 100:
            percent = 100

        rgb_image = self.convert('RGB')

        for x in range(0, self.width):
            for y in range(0, self.height):
                (r, g, b) = rgb_image.getpixel((x, y))

                self.putpixel((x, y), (int(r * (percent / 100)), int(g * (percent / 100)), b))

    # Turns the image grey by increasing all RGB values to the highest of the 3
    def bright_greyshift(self):
        rgb_image = self.convert('RGB')

        for x in range(0, self.width):
            for y in range(0, self.height):
                (r, g, b) = rgb_image.getpixel((x, y))

                highest = max(r, g, b)

                self.putpixel((x, y), (highest, highest, highest))

    # Turns the image grey by decreasing all RGB values to the lowest of the 3
    def dark_greyshift(self):
        rgb_image = self.convert('RGB')

        for x in range(0, self.width):
            for y in range(0, self.height):
                (r, g, b) = rgb_image.getpixel((x, y))

                lowest = min(r, g, b)

                self.putpixel((x, y), (lowest, lowest, lowest))
